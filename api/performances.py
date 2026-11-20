"""Official creator uploads. Playback stays in the official embedded player."""

def performance(id,icon,title,video,channel,language,format='song'):
    return dict(id=id,icon=icon,title=dict(en=title[0],hi=title[1]),youtube_id=video,channel=channel,
                available_languages=[language],original_language=language,format=format,source_kind='performance',
                source_url='https://www.youtube.com/watch?v='+video)

PERFORMANCES=[
 performance('performance-twinkle','⭐',('Twinkle Twinkle Little Star','ट्विंकल ट्विंकल लिटिल स्टार'),'yCjJyiqpAuU','Super Simple Songs','en'),
 performance('performance-wheels','🚌',('The Wheels on the Bus','व्हील्स ऑन द बस'),'yWirdnSDsV4','Super Simple Songs','en'),
 performance('performance-machli','🐟',('Machli Jal Ki Rani Hai','मछली जल की रानी है'),'VsEgpJTbW3s','Infobells - Hindi','hi'),
 performance('performance-nani','🦚',('Nani Teri Morni','नानी तेरी मोरनी'),'zkB47D6na_w','MaMa Monkey / Vianet Media','hi'),
 performance('performance-lakdi','🐴',('Lakdi Ki Kathi','लकड़ी की काठी'),'JX3dI6e1_2U','MaMa Monkey / Vianet Media','hi'),
 performance('performance-khilaunewala','🧸',('The Toy Seller','खिलौनेवाला'),'nOCi4LBZ6HA','NCERT OFFICIAL','hi','poem-performance'),
]
