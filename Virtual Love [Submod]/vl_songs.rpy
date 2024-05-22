init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_boytoy",
            prompt="Boy Toy",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_boytoy:
    m  1dub "{i}I've been going through changes,{/i}"
    m  1kub "{i}And I feel so elated,{/i}"
    m  1hub "{i}To be here in your big blue world.{/i}"
    m  1dud "{i}I know I'm not your favorite,{/i}"
    m  1duo "{i}But I like when you say it,{/i}"
    m  1hub "{i}I don't need you to be my girl~{/i}"

return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_mylove",
            prompt="My Love Mine All Mine",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_mylove:
    m  1dud "{i}Moon, tell me if I could,{/i}"
    m  1dkd "{i}Send up my heart to you?{/i}"
    m  1dkb "{i}So, when I die, which I must do...{/i}"
    m  1hkb "{i}Could it shine down here with you?{/i}"
return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_calmmedown",
            prompt="Calm Me Down",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.HAPPY,None)
        ),
        code="SNG"
    )

label mas_song_calmmedown:
    m  1dublb "{i}Use your body...{/i}"
    m  1dubsd "{i}Use it to put me to sleep~{/i}"
    m  1fubfb "{i}Your body, oh...{/i}"
    m  1dubfb "{i}Soothe my soul~{/i}"
    m  1kubfb "{i}So beautiful...{/i}"

return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_thisdec",
            prompt="This December",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_thisdec:
    m  1dud "{i}Only in my darkest moments can I see the light~{/i}"
    m  1dub "{i}I think I'm prone to getting blinded when it's bright...{/i}"
    m  1kub "{i}Well, this December, I'll remember,{/i}"
    m  1hublb "{i}Want you to see it when I do, ooh-ooh~{/i}"
    m  3hublb "{i}God knows I do!{/i}"

return
