"""Creator-hosted recordings of the published verses. Never extracted or re-uploaded."""


def recording(video, creator, language='en', style='song', **extra):
    return dict(youtube_id=video,channel=creator,language=language,style=style,source_url='https://www.youtube.com/watch?v='+video,**extra)


RECORDINGS = {
    'twinkle':recording('yCjJyiqpAuU','Super Simple Songs'),
    'baa-sheep':recording('XpvsJ4ANFp0','Mother Goose Club'),
    'mary-lamb':recording('YE7PiTwhTQk','Super Simple Songs'),
    'hickory':recording('HGgsklW-mtg','Super Simple Songs'),
    'hey-diddle':recording('sJiw-edttDY','Little Baby Bum'),
    'row-boat':recording('7otAJa3jui8','Super Simple Songs'),
    'humpty':recording('nrv495corBc','Super Simple Songs'),
    'rain-away':recording('c3v0rJqyCTM','Super Simple Songs'),
    'pat-cake':recording('jdg50KzCR9w','Super Simple Songs'),
    'little-bo-peep':recording('VS-P1QDKvNw','CoComelon'),
    'one-two-shoe':recording('FuZ9BiO4PQY','ChuChu TV'),
    'the-star':recording('eYPuGtWHUME','Little Learning Tales · Rima Patel','en','recitation'),
    'the-swing':recording('T42MKLGBv0I','Songs and Stories for the Classroom · Jim Shaw','en','song'),
    'rain-stevenson':recording('S8Rqqp5Zoik','Dr. Adam F. McCune','en','recitation'),
    'wind-stevenson':recording('TFLHGir2oSY','LibriVox Audiobooks · Crystal F.','en','recitation',end=81),
    'bed-summer':recording('2IRUoXp1xxQ','Jordan Harling Reads','en','recitation'),
    'utho-lal':recording('h6g2W0k3hhQ','ZappyToons','hi'),
    'koyal-hariaudh':recording('d4w4awGjH9o','Jeevan Aayam · Nandini P. Sharma','hi','recitation'),
    'kabir-kind-words':recording('tdbtKvLR2VU','Sanskar Music · Vidhi Sharma','hi'),
    'kabir-patience':recording('x-kfOV1vBOw','Saregama Bhakti · Baiju Mangeshkar','hi'),
    'rahim-love':recording('e2m1Xa8HsTc','Suresh Wadkar','hi'),
    'kadamb-tree':recording('hw0zo37RzhI','Usha Verma','hi','recitation'),
}
