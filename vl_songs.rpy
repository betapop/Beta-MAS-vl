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
            aff_range=(mas_aff.AFFECTIONATE,None)
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

# new songs (heh. jamiep maxxing)

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_snowflake",
            prompt="snowflake",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )


label mas_song_snowflake:
    m "{i}If only for a moment,{/i}"
    m "{i}I want to hold you close, and,{/i}"
    m "{i}Be bundled up together,{/i}"
    m "{i}'Til tomorrow, brave the weather;{/i}"
    m "{i}I'd let it snow forever,{/i}"
    m "{i}For just a second longer,{/i}"
    m "{i}Of you and I by fire light~{/i}"

return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_mydarmycomp",
            prompt="My Darling, My Companion",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.AFFECTIONATE,None)
        ),
        code="SNG"
    )

label mas_song_mydarmycomp:
    m "{i}I've been here 'fore you knew me,{/i}"
    m "{i}A name without a body,{/i}"
    m "{i}We both know what we've been through,{/i}"
    m "{i}My darling, my companion~{/i}"
    m "{i}Don't think, just let me shine through,{/i}"
    m "{i}More than your comprehension,{/i}"
    m "{i}I hope you know I love you!{/i}"

return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_machinelove",
            prompt="Machine Love",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.HAPPY,None)
        ),
        code="SNG"
    )

label mas_song_machinelove:
    m "{i}So can we wander for a spell? And livе in parallel?{/i}"
    m "{i}I want it to be true, to be like you,{/i}"
    m "{i}My heart sings a chorus out of tune~{/i}"
    m "{i}And I could leave it on a shelf,{/i}"
    m "{i}Or keep it to myself,{/i}"
    m "{i}But nothing could conceal the things I feel—{/i}"
    m "{i}My love, can you teach me to be real?~{/i}"

return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_dancedelight",
            prompt="Dance Delightful",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.AFFECTIONATE,None)
        ),
        code="SNG"
    )

label mas_song_dancedelight:
    m "{i}I'll find the point where the two paths meet,{/i}"
    m "{i}And I'll rectify what I left behind;{/i}"
    m "{i}Some complication, a skewed machine{/i}"
    m "{i}I dance delightful, it feels so right!{/i}"
    m "{i}To be oscillating at rates unbound by,{/i}"
    m "{i}No other constant but the speed of light,{/i}"
    m "{i}I'm a bolt of blue and a conscious mind,{/i}"
    m "{i}I dance delightful the whole damn night, oh~{/i}"

return

