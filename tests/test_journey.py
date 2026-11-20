import sqlite3
import unittest
from datetime import datetime, timedelta, timezone

from api import journey


class SunshineTrail(unittest.TestCase):
    def setUp(self):
        self.con=sqlite3.connect(':memory:')
        self.con.row_factory=sqlite3.Row
        self.con.execute('PRAGMA foreign_keys=ON')
        self.con.execute('CREATE TABLE children(id INTEGER PRIMARY KEY)')
        self.con.executemany('INSERT INTO children VALUES(?)',[(1,),(2,)])
        journey.schema(self.con)
        self.start=datetime(2026,1,1,12,tzinfo=timezone.utc)

    def tearDown(self):
        self.con.close()

    def day(self,offset):
        return self.start+timedelta(days=offset)

    def state(self,day=0,child=1,**kwargs):
        return journey.snapshot(self.con,child,now=self.day(day),**kwargs)

    def learn(self,day=0,key='please',child=1):
        journey.record(self.con,child,'lesson',key,now=self.day(day))
        return self.state(day,child)

    def test_opening_does_not_start_streak(self):
        first=self.state()
        self.assertEqual((first['streak'],first['balance'],first['shields']),(0,20,1))
        self.assertFalse(first['learned_today'])
        self.assertEqual(self.state(8)['shields'],1)

    def test_daily_learning_and_missed_day_protection(self):
        self.assertEqual(self.learn()['streak'],1)
        protected=self.state(2)
        self.assertEqual((protected['streak'],protected['shields']),(1,0))
        self.assertEqual(protected['protected_days'],1)
        self.assertTrue(next(b for b in protected['badges'] if b['id']=='shield-friend')['earned'])
        self.assertEqual(self.learn(2)['streak'],2)
        self.assertEqual(self.state(4)['streak'],0)
        fresh=self.learn(4)
        self.assertEqual((fresh['streak'],fresh['best']),(1,2))

    def test_protection_does_not_increase_learning_days(self):
        self.learn(0)
        journey.credit(self.con,1,'gift',200,'welcome',self.day(0).date())
        journey.buy_shield(self.con,1,'first-purchase',now=self.day(0))
        journey.buy_shield(self.con,1,'second-purchase',now=self.day(0))
        protected=self.state(4)
        self.assertEqual((protected['streak'],protected['protected_days'],protected['shields']),(1,3,0))
        self.assertEqual(self.learn(4)['streak'],2)

    def test_buying_after_gap_does_not_restore_old_streak(self):
        self.learn(0)
        self.state(3)
        journey.credit(self.con,1,'gift',100,'welcome',self.day(3).date())
        journey.buy_shield(self.con,1,'late-purchase',now=self.day(3))
        state=self.state(3)
        self.assertEqual((state['streak'],state['shields']),(0,1))
        self.assertEqual(self.state(4)['shields'],1)

    def test_repeat_rewards_and_daily_caps(self):
        one=self.learn()
        self.assertEqual(self.learn()['balance'],one['balance'])
        for index in range(9):
            self.learn(key='lesson-'+str(index))
        count=self.con.execute("SELECT COUNT(*) FROM journey_ledger WHERE reason='lesson'").fetchone()[0]
        self.assertEqual(count,5)
        self.assertEqual(self.state()['streak'],1)
        self.assertEqual(self.learn(1)['streak'],2)

    def test_game_improvement_can_finish_mission_without_repeat_activity_reward(self):
        journey.record(self.con,1,'game','habit:1',{'score':0,'level':1},now=self.day(0))
        initial=self.state()
        self.assertEqual(initial['streak'],1)
        journey.record(self.con,1,'game','habit:1',{'score':3,'level':1},now=self.day(0))
        improved=self.state()
        self.assertEqual(improved['balance']-initial['balance'],18)
        self.assertEqual(self.con.execute("SELECT COUNT(*) FROM journey_ledger WHERE reason='game'").fetchone()[0],1)

    def test_missions_difficulty_and_rewards_are_stable(self):
        initial=self.state(challenge=3)
        challenge=next(item for item in initial['missions'] if item['id']=='brave-practice')
        self.assertIn('3',challenge['title']['en'])
        journey.record(self.con,1,'game','habit:3',{'score':2,'level':3},now=self.day(0))
        complete=self.state(challenge=1)
        self.assertTrue(next(item for item in complete['missions'] if item['id']=='brave-practice')['completed'])
        self.assertEqual(self.state()['balance'],complete['balance'])
        self.assertTrue(all(not mission['completed'] for mission in self.state(1)['missions']))

    def test_reading_gives_seeds_but_not_learning_streak(self):
        journey.record(self.con,1,'reading','stories:lion-mouse:hi',now=self.day(0))
        read=self.state()
        self.assertEqual((read['streak'],read['balance']),(0,29))
        journey.record(self.con,1,'reading','stories:lion-mouse:hi',now=self.day(0))
        self.assertEqual(self.state()['balance'],29)

    def test_shield_cost_cap_and_purchase_retry(self):
        self.state()
        with self.assertRaises(journey.JourneyError):
            journey.buy_shield(self.con,1,'no-money',now=self.day(0))
        journey.credit(self.con,1,'gift',100,'welcome',self.day(0).date())
        journey.buy_shield(self.con,1,'same-purchase',now=self.day(0))
        bought=self.state()
        journey.buy_shield(self.con,1,'same-purchase',now=self.day(0))
        self.assertEqual(self.state()['balance'],bought['balance'])
        self.assertEqual(bought['shields'],2)
        journey.buy_shield(self.con,1,'another-purchase',now=self.day(0))
        with self.assertRaises(journey.JourneyError):
            journey.buy_shield(self.con,1,'full',now=self.day(0))

    def test_badge_reward_once_and_independent_children(self):
        self.state()
        badge={'id':'first-spark','earned':True}
        first=self.state(base_badges=[badge])
        self.assertEqual(first['balance'],35)
        self.assertEqual(self.state(base_badges=[badge])['balance'],35)
        self.assertEqual(self.state(child=2)['balance'],20)
        self.learn(child=1)
        self.assertEqual(self.state(child=2)['streak'],0)

    def test_timezone_uses_local_midnight_and_is_not_changed_by_later_headers(self):
        before=datetime(2026,1,1,18,29,tzinfo=timezone.utc)
        after=before+timedelta(minutes=2)
        journey.snapshot(self.con,1,zone='Asia/Kolkata',now=before)
        journey.record(self.con,1,'lesson','please',now=before)
        journey.record(self.con,1,'lesson','please',now=after)
        result=journey.snapshot(self.con,1,zone='America/New_York',now=after)
        self.assertEqual(result['day'],'2026-01-02')
        self.assertEqual(result['timezone'],'Asia/Kolkata')
        self.assertEqual(result['streak'],2)

    def test_streak_badges_require_real_learning_days(self):
        for day in range(3):
            result=self.learn(day)
        self.assertTrue(next(b for b in result['badges'] if b['id']=='streak-3')['earned'])
        self.assertFalse(next(b for b in result['badges'] if b['id']=='streak-7')['earned'])


if __name__=='__main__':
    unittest.main()
