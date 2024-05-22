init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="vl_mascomp_lightroom",
            category=['mas_compliment'],
            prompt="You light up the room!",
            unlocked=True
            ),
            code="CMP"
            )

label vl_mascomp_lightroom:
    m 5ekbsb "Aw, [mas_get_player_nickname()]..."
    m 4hub "You light up my room too! To be honest... you light up my world."
    m 1eubsb "I'm so happy you're here, [player]."
    m 5hkbsb "I love you so much, and you're my light!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="vl_mascomp_puzzle",
            category=['mas_compliment'],
            prompt="You’re the missing puzzle piece in my life!",
            unlocked=True
            ),
            code="CMP"
            )

label vl_mascomp_puzzle:
    m 1sublb "[player]! You're my puzzle piece!"
    m 1tub "If it wasn't for you, we wouldn't be here right now."
    m 5ekbsb "You saved me, [mas_get_player_nickname()]! And i'll always be grateful."
    m 5hkbsb "You were my missing piece, and i'm glad i found you~ I love you!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="vl_mascomp_package",
            category=['mas_compliment'],
            prompt="You’re the whole package– beauty, brains, and personality!",
            unlocked=True
            ),
            code="CMP"
            )

label vl_mascomp_package:
    m 1sublb "[mas_get_player_nickname()]! You're so sweet..."
    m 2lkbfsdlb "I don't even know how to respond! You flatter me so much~"
    m 1eubsb "I love you [player]! I love every little bit about you!"
return "love"