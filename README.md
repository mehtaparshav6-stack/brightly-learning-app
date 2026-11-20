# Brightly

**Small steps, bright futures.** Brightly is a parent-managed learning garden for children aged 3–7. Its lessons, stories, rhymes, poems, and games teach kindness, good habits, friendship, and everyday skills in English, Hindi, and Marathi.

This is a standalone project. No Brightly source repository or Base44 export was included with the brief, so the application uses React, esbuild, React Three Fiber, FastAPI, and SQLite. The public welcome page has a pointer- and scroll-responsive 3D garden. The learning workspace uses simpler controls suited to young children.

## Run locally

Use Python 3.12 and Node.js 22 or newer. From the project root:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cd web
npm ci
npm run build
cd ..
python -m uvicorn api.main:app --host 127.0.0.1 --port 8000
```

Open <http://127.0.0.1:8000>. For frontend development, keep the API on port 8000 and run `cd web && npm run dev` in another terminal. That command watches source files and rebuilds assets; refresh the browser to see changes. The packaged project includes a built `web/dist`, so after installing Python dependencies the production site can start without Node; rebuild after editing frontend files. `npm install` reports zero known vulnerabilities for the included dependency set.

## What works

- Parent signup and login with salted PBKDF2-SHA256 password hashes, HttpOnly session cookies, a CSRF token on authenticated changes, a login-attempt limit, and a one-time recovery code for password resets. Save that code when it appears: Brightly deliberately does not collect or configure an email service.
- Up to eight private child profiles per parent, with age, language, and symbol; profile editing and deletion.
- Fifty translated lessons across four categories; server-checked questions; level unlocks only from successfully completed lessons. A wrong answer gives another chance without recording completion.
- Fourteen mini games with three difficulties each, twenty-four complete moral stories, eleven traditional rhymes, eleven credited poems, and six official video performances. Pattern, tap-to-count, rhyming, sequencing, shape, comparison, and number-path games add step-by-step practice. See [Content sources](CONTENT_SOURCES.md) for the inspiration behind the new activities.
- Correct/incorrect feedback with explanations in every quiz game, optional retry, and an explicit next-question button. Game stars count first answers; retries teach the answer without rewriting the first-try score. Zero, partial, and perfect scores have different messages. Memory games explain mismatches and award stars only after matching every pair.
- Each game has three difficulties. At least two stars at the previous difficulty unlock the next, with the best result saved per difficulty. Memory grows from three pairs to four and six. The server validates unlocks and selected banks. Old game results count as difficulty one.
- A next-lesson action after completion uses the updated unlock level and skips completed lessons. Progress totals follow the actual curriculum size.
- Saved daily habit check-ins, habit-practice day totals, and a downloadable SVG or printable certificate when every lesson is complete. Habit check-ins are self-reported practice, kept separate from quiz stars.
- Saved completions, game history, stars, child progress, and a parent overview. Thirty-two achievement badges track lesson completion, good-habit lessons, different games played, perfect scores, and memory pairs. Previously saved progress counts toward these achievements. Earning a badge opens a celebration dialog with a chime and an explicit Keep growing button. A single dialog can show multiple newly earned badges. Data persists in SQLite through refreshes and sign-outs.
- The header language switch immediately updates the text and narration and saves the selected language to the active child’s profile. Selecting a child uses that child’s saved language, including after refresh or parent profile edits; an older browser language choice cannot override it. The public pages remember their language on the current device. New full stories and credited poems have English and Hindi editions. The reader shows an explicit English fallback for Marathi profiles. Marathi lessons and previously translated nursery rhymes remain available.
- Lesson questions, all answer choices, practice activities, game instructions, and game questions have listening controls using the same neural voices as the stories. Numbered choices connect spoken answers to the buttons. The speaker beside a choice reads it without selecting it. Playback pauses/resumes, and starting another reading, changing language, or leaving an activity stops the previous voice. English and Hindi activity audio is prepared in `media/narration/` as part of this distribution.
- The Sound & voice menu has a saved tap/answer sound toggle, volume, reading pace, and matching voice selection. Meaningful feedback is also shown in text and brief visual cues.
- Desktop and mobile layouts, keyboard focus states, semantic form labels, reduced-motion support, and a static fallback for the 3D garden.

## Storytelling and voice settings

The default narrator uses Microsoft Edge neural speech through `edge-tts==7.3.1`. It needs no paid speech key. English uses Sonia, Hindi uses Swara, and Marathi uses Aarohi. All 103 reading-library tracks (about 91 minutes) are prepared in `media/narration/` and included in the project archive. These are synthetic neural voices. Built-in text is sent to the online service when generating an uncached reading. The app plays complete buffered audio and preserves the position through pause/resume.

Choose **Listen together** in a story or lesson. Poems and rhymes use **Listen to the original recording** instead. Volume and pace are available in **Sound & voice**. The device voice is an explicit fallback. It depends on installed speech voices. Bundled English/Hindi speech is used first even if an optional provider account is unconfigured or its model/voice settings differ. A zero-volume setting shows a localized Turn on voice action rather than silently appearing to play. Uncached new text needs an internet connection and the online service may be unavailable. The Edge client is a community client for an online service, and its availability can change. See the [client documentation](https://github.com/rany2/edge-tts).

To regenerate the reading-library tracks, run `BRIGHTLY_TTS_PROVIDER=edge python scripts/build_library_audio.py` from the project root. The command skips existing tracks and writes a track index. `python -m api.prepare_audio --kind stories --id lion-mouse --language hi --mode spoken` prepares one reading.

To regenerate the lesson and game recordings, run `python scripts/build_activity_audio.py`. Repeated options and instructions share the same recording. The script skips existing files, writes `media/narration/activities.json`, and does not remove the story recordings. Only approved published content can be requested from the narration API; the client cannot supply arbitrary speech text.

Optional OpenAI narration remains available by configuring `OPENAI_API_KEY`. Set `BRIGHTLY_TTS_PROVIDER=auto` to choose it automatically when a key is present. The default remains Edge neural speech. Bundled speech still takes priority with either provider. To deliberately use a custom provider instead of the bundled tracks, set `BRIGHTLY_USE_BUNDLED_AUDIO=0` and `BRIGHTLY_TTS_PROVIDER=openai`. OpenAI narration uses Marin with gentle storytelling instructions. `BRIGHTLY_TTS_MODEL` and `BRIGHTLY_TTS_VOICE` configure that integration. Provider charges may apply.

## Songs and original performances

The **Watch & listen** filter includes official creator uploads for familiar English and Hindi songs and an NCERT poem performance. They play in a visible YouTube privacy-enhanced embedded player after pressing Play. The creator is credited and an Open on YouTube link is provided if embedding is blocked. Availability, advertisements, and recommendations remain controlled by YouTube. The project does not extract or redistribute their soundtracks.

Every one of the 22 text poems and rhymes now has a creator-hosted recording selected in `api/recordings.py`. The Listen action opens that original recording, with no generated singing or linked voice account. Traditional nursery songs use recorded singing; literary poems use a credited song performance or recitation. The original recording keeps its original language, which is shown alongside the credit. A Brightly translation can be read below it, but is not presented as an original recorded translation. The external player loads only after a click, supports native playback controls, closes when switching language or leaving, and includes a direct creator link if embedding is unavailable. Recordings require internet; provider availability and advertising remain outside Brightly’s control. The advanced singing API remains for compatibility, but is not offered in the child-facing library.

## Reading achievements

**We finished this together** records the first completion per child, reading, and language, and a separate daily reading check-in. A reading can be completed again on a later day for its daily mission and eligible Sunseeds. It is a family check-in, and contributes to reading badges without adding quiz stars. Repeated saves preserve the first completion. Reading in both English and Hindi unlocks the bilingual badge. Other new badges celebrate five, ten, and twenty stories, poetry milestones, reading from different collections, balanced lesson practice, and advanced games. The achievement popup uses its own six-note bell flourish and respects the sound and volume settings.

## Sunshine trail: streaks, Sunseeds, and shields

The dashboard and **Streak & missions** page show a learning streak, best streak, a seven-day calendar, Sunseeds, shield inventory, and four daily missions. These are separate from self-reported household habits. Completing a lesson quiz correctly or finishing a mini game qualifies a learning day; opening the app or checking a habit does not. A finished game counts as practice even if its first-try score is zero. Repeating a lesson on a different day can keep the streak going.

The server chooses the day in the child's IANA time zone, captured from the first device request when the wallet is created. Later requests cannot change it or submit a backdated learning day. Days reset at local midnight. The page refreshes when the app becomes visible and periodically while open. Existing accounts and learning progress are preserved; the new learning-day calendar starts with this update, and previously earned achievements receive their one-time Sunseed bonus.

A new wallet starts with **20 Sunseeds and one shield**. One shield costs **40 Sunseeds**, with a maximum of **three** in the pouch. Shields are used automatically for consecutive missed days while a streak is alive. They preserve continuity without adding a learning day. If the gap is longer than the available shields, the current streak resets and the best streak remains. Buying a shield after a missed, unprotected day cannot restore the old streak.

Sunseed rewards are server-owned and recorded in an idempotent ledger:

| Activity | Reward | Daily reward limit |
| --- | --- | --- |
| Different completed lessons | 12 each | First 5 |
| Different game/difficulty combinations | 6 + twice the first saved score + 3 per difficulty above one | First 5 |
| Different reading/language combinations | 3 each | First 3 |
| Newly earned achievement | 15 | Once per badge |
| Daily lesson mission | 20 | Once |
| Daily game mission | 10 | Once |
| Daily reading mission | 6 | Once |
| Daily two-star challenge mission | 18 | Once |

The lesson mission rotates between two, three, and five different lessons. The challenge uses the highest game difficulty already unlocked when that day's missions are first created, so a new learner is not assigned a locked difficulty. Improving a game later that day can finish a mission without collecting its activity reward twice. Missions pay automatically, refresh the next day, and impose no penalty when unfinished. Sunseeds never cost real money and spending them does not remove learning stars. Purchase retries cannot spend twice, concurrent purchases cannot overdraw a wallet, and inventory is capped in the database.

Seven new achievements recognize 3-, 7-, 14-, and 30-learning-day streaks, a shield-protected day, and five or twenty daily missions. A streak badge counts actual learning days within one protected chain. The badge popup also shows its Sunseed reward.

## Data and privacy

SQLite data is stored in `brightly.sqlite3` by default. Set `BRIGHTLY_DB_PATH` to use a different location. The database, virtual environment, Node dependencies, and npm cache are ignored by Git. Child profile data stays local to the server and is scoped to the signed-in parent; there are no public profiles or chat. External YouTube players load only after the Play action and may show advertisements controlled by YouTube. Only the parent is authenticated; a young child's view is selected inside the parent's session. For public deployment, use HTTPS and set `BRIGHTLY_HTTPS=1` so session cookies have the Secure flag. Protect and back up the database, and add an operational privacy policy before collecting real children's information online.

The learning library is an original curriculum with adapted traditional readings, not a medical or developmental assessment. The 3D scene is decorative and the learning activities remain usable without WebGL. Bundled neural recordings play without installed device voices. Device-voice fallback uses the installed voices. The written content is always available. Video lessons are not bundled because no video assets were supplied; the lessons use original illustrated text and interactive questions instead.

## Verification

The project was built with `npm run build` and checked in a local browser through signup → child creation → lesson quiz → saved progress after reload → password recovery → sign-in. The browser reported no page errors at desktop or mobile widths. The Python API was also started with Uvicorn and served the built homepage successfully.

## Updating an existing Brightly installation

Stop the running server, replace the source and `web/dist` with this version, install the updated dependencies with `python -m pip install -r requirements.txt`, then restart the server. Keep your existing `brightly.sqlite3` file (or the file selected by `BRIGHTLY_DB_PATH`): it contains accounts and progress. This archive contains no user database. New tables, including the journey wallet, ledger, daily missions, learning days, and reading progress, and the game-attempt and game-level columns are added automatically without deleting existing data. Replaying a completed lesson no longer changes its first-completion date. Failed game saves can be retried without duplicating rewards.

## Regression tests

Run the API suite from the project root with `.venv/bin/python -m unittest discover -s tests -v`. It starts an isolated server and temporary database. It covers scoring, per-answer feedback, retry idempotence, lesson gates, reading persistence and badges, content completeness, translations, habit persistence and ownership protections.

For the browser suite, install its optional test dependencies with `npm install --prefix tests`, start an isolated API on port 8877 with `BRIGHTLY_USE_BUNDLED_AUDIO=0 BRIGHTLY_TTS_PROVIDER=openai OPENAI_API_KEY='' ELEVENLABS_API_KEY='' BRIGHTLY_DB_PATH=/tmp/brightly-tests.sqlite3 python -m uvicorn api.main:app --port 8877`, and run `npm test --prefix tests`. Installed Google Chrome is used. `BRIGHTLY_TEST_URL` can select a different local URL. The suite creates test accounts: use a disposable database via `BRIGHTLY_DB_PATH`. It checks badge-dialog dismissal, continuous device utterances, buffered audio pause/resume using a local WAV fixture, original verse recording activation, library search, saved difficulty unlocks, and zero/partial/perfect scores, wrong-answer retry, memory mismatch, next lessons, saved habits, the Rewards page, certificate downloads, the Hindi language switch, voice selection and pause/resume with controlled speech doubles, answer sound and mute, achievement notifications, the sequence game, and mobile width. `BRIGHTLY_PLAYWRIGHT` optionally points to an existing Playwright installation.

For a check using the actual bundled voice files, start an isolated server on port 8878 with `BRIGHTLY_TTS_PROVIDER=edge` and run `BRIGHTLY_TEST_URL=http://127.0.0.1:8878 node tests/narration.cjs` after installing the browser test dependency. This check plays both English and Hindi through the authenticated audio endpoint, verifies the durations, and checks pause/resume without making another narration request.

`node tests/activity-voice.cjs` checks the Hindi preference regression, profile edits, persistence, rapid language switching, lesson/game questions and choice audio, independent child languages, mobile layout, and prevention of overlapping voices or accidental answer submission. It uses a local audio fixture by default. Run `BRIGHTLY_REAL_AUDIO=1 BRIGHTLY_TEST_URL=http://127.0.0.1:8878 node tests/activity-voice.cjs` against the isolated Edge server to exercise real neural recordings instead. As with the other browser tests, use a disposable database because the test creates parent and child accounts.


`node tests/journey.cjs` checks the new streak page, mission payouts, shield purchases and retry protection, inventory limits, original poem playback without a narration request, and Hindi/mobile layouts. Optionally set `BRIGHTLY_TEST_DB` to the **same disposable database** as the test server to populate a protected-day calendar fixture. Never point that option at a real family database. Date-based Python tests simulate missed days, shield exhaustion, learning-day counts, mission rollover, and local midnight; the API suite also tests private wallets and concurrent purchases. Real audio checks have passed with an intentionally unconfigured OpenAI account because the English/Hindi bundle is served first.

`node tests/original-recordings-live.cjs` performs an optional internet-dependent check of real English and Hindi creator players, including increasing media playback time. Other player tests use a local iframe fixture so they do not depend on network availability or advertisements. It creates disposable test accounts.
