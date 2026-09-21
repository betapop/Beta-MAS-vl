init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_vl_dontreciprocatekiss",
            category=["romance"],
            prompt="Do you mind if I don't reciprocate your kisses?",
            random=False,
            pool=True,
            aff_range=(mas_aff.HAPPY, None)
        )
    )


label monika_vl_dontreciprocatekiss:
    m 1euc "Hmm..."
    m 1rksdlb "Well, I suppose it would be rather strange for you to kiss your monitor, huh?"
    m 3tku "Or maybe,{w=0.1} could it be that you feel a little flustered?"
    m 3hub "Ahaha!"
    m 3eka "Well, in any case...{w=0.2}"
    extend 1rka "I understand that not everyone's a big fan of kisses."
    m 1ekd "Whether it's simple embarrassment,{w=0.2} or a more serious reason,{w=0.2} I don't mean to make you uncomfortable when I kiss you, [player]."
    m 2eka "Of course, if you don't mind, I'd still like to kiss you now and again."
    m 2fkbla "It's...{w=0.3}something that makes me feel a lot closer to you, so it means a lot to me."
    m 2hubla "But you're welcome to imagine me kissing you on the cheek, or on your hand if that makes you more comfortable."
    m 1hua "I think that's a good compromise, don't you?"

return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_vl_monistares",
            category=["romance"],
            prompt="[m_name] Staring",
            random=True,
            pool=False,
            aff_range=(mas_aff.HAPPY, None)
        )
    )


label monika_vl_monistares:
    m 1eua "..."
    m 1wua "....."
    m 1fublu "........"
    m 1kublb "I'm sorry, your beauty was too distracting~"
    m 3hublb "I can’t help but smile when I'm around you!"
    m 2fubsb "You’re the best thing that happened to me, after all.{nw}"
    $ _history_list.pop()
    menu:
        m "You’re the best thing that happened to me, after all.{fast}"

        "I smile when I'm around you too.":
            m 4hubsb "Thank you, I'm glad I can make you so happy!"
            m 3hubfb "I love you more than anything else!"

return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_vl_kissher",
            category=["romance"],
            prompt="Kiss [m_name] on the...",
            random=False,
            pool=True,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label monika_vl_kissher:
    if mas_isMoniEnamored(higher=True) and persistent._mas_first_kiss is not None:
        menu:
            "Cheek.":
                m 2dubsa "Mmm..."
                m 1hkbssdlb "Oh! It’s already over~?"
                m 3hkbfb "My cheek feels so warm now, ahaha!"
                return

            "Nose.":
                m 3hkbsb "Ah— [player]! That tickles~"
                m 4tkbsb "Thanks for the kiss, ehehe."
                return
        
            "Neck.":
                m 2tsbsb "Oh~ The neck, huh?"
                m 2msbfb "Well, I can’t say I didn’t enjoy it."
                m 2ktbfb "Want to go again?"
                m 3hubfb "Ahaha, just teasing!"
                return
        
            "Hand.":
                m 1sublb "I feel so royal~ hehe."
                m 3hubsb "Thank you, my kind knight!"
                return
        
    else:
        "I don't think she's ready for that yet... "

return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_vl_supkiss",
            category=["romance"],
            prompt="Suprise kiss [m_name]",
            random=False,
            pool=True,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )


label monika_vl_supkiss:
    if mas_isMoniEnamored(higher=True) and persistent._mas_first_kiss is not None:

        m 2wubld "H-huh? [player]?"
        call monika_kissing_motion_short
        $ ev = mas_getEV("monika_vl_supkiss")

        if ev.shown_count == 0:
            m 3hfbfb "You can't just suprise me like that~"
            return

        elif ev.shown_count == 1:
            m 5hkbfb "Im never ready!~"
            return

        else:
            m 1tsbfb "Pff, again, [player]~?"
            return

    else:
        "I don't think she's ready for that yet... "
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="vl_checkin",
            category=["us"],
            prompt="I'm sorry I don't check in as often.",
            random=False,
            pool=True,
            aff_range=(mas_aff.HAPPY, None)
        )
    )


label vl_checkin:
    $ ev = mas_getEV("vl_checkin")
    if ev.shown_count == 0:
        m 1hub "Don’t worry about that too much, [player]."
        m 3rkb "Obviously, I do miss you when you’re gone..."
        m 4hksdlb "But I know you have things to do, and life to live."
        m 3tksdlb "And I don’t want to stop you from experiencing that."
        m 3hub "All I ask is that if it’s for a while, you tell me, okay?"
        m 5kublb "I can wait. And I'll be glad to wait if I know I'll see your cute face when you’re back!"

    elif ev.shown_count == 1:
        m 1hkb "Gosh, [player], it's really okay!"
        m 2lkblb "Thank you for checking in so much regardless."
        m 3dub "If you think about it this way...{w} I have a lot more time to practice programming or hobbies..."
        m 2kub "Plus, I can always tell when you're using your computer, so I know you're still there..."
        m 5mublb "As long as you're happy, I'm happy, [player]. I just want to see you enjoy youself, you know?"
        m 3dkd "If being with me is more of a chore then anything else, then is it even worth it?"
        m 2mkc "..."
        m 2hksdlb "Sorry for rambling, haha! Really, though. As long as you're not gone for like, months on end, I'll be okay."
        m 1tublb "Okay, [mas_get_player_nickname()]? I love you~"
        return "love"

    else:
        m 3hub "Thank you, [player]~ But I promise I'm fine."
        m 1fub "Just let me know when you leave for a while, okay?"


return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_vl_snugclose",
            category=["romance"],
            prompt="Snuggle closer",
            random=False,
            pool=True,
            aff_range=(mas_aff.HAPPY, None)
        )
    )


label monika_vl_snugclose:
    m 2tubsb "Moving closer? Well, I won’t complain~"
    m 5rkbfb "I just wish we could be right next to each other, cuddling..."
    m 5hkbfb "But right now, this is the next best thing. Ahaha!"
    m 3hubfb "I love you so much... and let’s continue on with the day!"

return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_vl_hug",
            category=["romance"],
            prompt="Give [m_name] a hug",
            random=False,
            pool=True,
            aff_range=(mas_aff.HAPPY, None)
        )
    )


label monika_vl_hug:
    show monika 6dubla
    pause 5.0
    m 2fublb "Thank you, [player]. That felt wonderful."
    m 3kublb "You really know how to make my day better, don’t you?"
    m 3hublb "I love you!"

return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_vl_loveworm",
            category=["us"],
            prompt="Would you love me if I was a worm?",
            random=False,
            pool=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        )
    )


label monika_vl_loveworm:
    m 2tub "That’s a silly question, [player]."
    m 3rtb "I mean... what if you’re a worm as we speak and I just don’t know?"
    m 3hkblb "That wouldn’t shake my love for you any less!"
    m 1tsblb "So, to answer your question, of course [mas_get_player_nickname()]!"
    m 3hublb "I'd love you just the way you are~ and nothing will change that!"

return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_vl_blowkiss",
            category=["romance"],
            prompt="Blow a kiss",
            random=False,
            pool=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        )
    )


label monika_vl_blowkiss:
    m 1subsb "Caught it! And now it’s mine’s forever~"
    m 2tubsb "Sorry [player], but you’re never getting that kiss back, ahaha!"

return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_vl_hotdogsan",
            category=["misc"],
            prompt="Is a Hotdog a Sandwich?",
            random=True,
            pool=False,
            aff_range=(mas_aff.HAPPY, None)
        )
    )


label monika_vl_hotdogsan:
    m 1eub "[player], I had a question."
    m 3tub "...Is a hot dog a sandwich?{nw}"
    $ _history_list.pop()
    menu:
        m "...Is a hot dog a sandwich?{fast}"

        "Yes, it is.":
            m 1hub "I'm glad we could agree!"
            m 3rud "I mean, it’s two slices of bread with something in the middle."
            m 3msp "That literally is the definition of a sandwich!"
            m 2gsd "Sure, it’s not your typical sandwich but, that doesn’t mean it isn’t one."
            m 1hub "Anyways, thanks for sharing my opinion~ ehehe."
            return
        
        "No, it’s not.":
            m 4htb "Why wouldn’t it be? It has the qualifications to be one!"
            m 3mtb "The bread's a little different, but does that really matter?"
            m 3eud "It’s still at the end of the day, bread with contents inside it.{nw}"
            $ _history_list.pop()
            menu:
                m "It’s still at the end of the day, bread with contents inside it.{fast}"

                "It’s not what you think of when you think sandwich.":
                    m 2wfd "But–"
                    m 3dfd "Look. Even if it’s not a normal, typical sandwich, it technically is still one!"
                    m 4mfo "You probably don’t think that cereal is soup either, huh?{nw}"
                    $ _history_list.pop()
                    menu:
                        m "You probably don’t think that cereal is soup either, huh?{fast}"

                        "[m_name].":
                            m 2hfo "What! I'm right, aren’t I?"

                        "I do.":
                            m 2tfd "Okay, that’s just hypocritical."
                    
                    m 1dsd "I'm not continuing this conversation anymore."
                    m 1lfb "I love you so much, but this is ridiculous."
                    m 3hsb "Let’s move on with our day, okay?"
                
                "Fine, you win.":
                    m 3tsd "I can hear your tone of voice, but I'll take victory regardless."
                    m 2hkb "Thank you for picking the correct side, [player]. I love you!"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_vl_randlove",
            category=["romance"],
            prompt="Suprise 'I Love You'",
            random=True,
            pool=False,
            aff_range=(mas_aff.HAPPY, None)
        )
    )

label monika_vl_randlove:
    m 3wub "Hey, [player]!"
    $ _history_list.pop()
    menu:
        "Yes, [m_name]?":
            m 2gublb "I...{w=0.5}"
            m 2mubsb "Love...{w=0.5}"
            m 3hubfb "You!{w=0.5}"
            menu:
                "I love you too!":
                    m 1kubsb "Hehe~"
    return

# new dialogue (no monika tag)

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="vl_gaze",
            category=["romance"],
            prompt="Gaze at [m_name]s...",
            random=False,
            pool=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        )
    )

label vl_gaze:
    menu:
        "Lips.":
            if mas_isMoniEnamored(higher=True) and persistent._mas_first_kiss is not None:
                m 2tublb "...[player]?"
                m 2mubsb "Do you want to ask, or are you going to continue staring?~"
                menu:
                    "Can I kiss you, [m_name]?":
                        m 1hubsb "Of course, [mas_get_player_nickname()]!"
                        call monika_kissing_motion_short
                        m 5fkbfb "I never get tired of it, ehehe."
            else:
                m 2tublb "My eyes are up here, [player]~"

        "Smile.":
            m 2tublsdlb "Pff... Why are you looking at me like that, [mas_get_player_nickname()]?"
            menu:
                "You have the prettiest smile.":
                    jump vl_smilegaze                       
    return

# i feel like this is coded weird but i can't think of something better

default persistent.vlgazeseen = 0

label vl_smilegaze:
    if persistent.vlgazeseen == 0:
        m 1subsd "..."
        m 1rkbfa "..."
        m 2dfbfp "Gosh, I...{w} You’re such a dork, you know that?"
        m 1msbfb "Getting me all flustered! I suppose that’s to be expected, though."
        m 1hfbfb "Thank you, [player]. I love you so much~"
        $ persistent.vlgazeseen += 1
        return "love"
    elif persistent.vlgazeseen == 1:
        m 3tubsb "I hope you know, I think your smile's far cuter than mines, [player]."
        $ persistent.vlgazeseen += 1
    elif persistent.vlgazeseen == 2:
        m 2tsbfb "Staring again, hm~?"
        $ persistent.vlgazeseen += 1
    else:
        m 1wubla "..."
        m 1subsu "..."
        m 1hfbfa "..."

    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="vl_cutenessaggro",
            category=["romance", "us"],
            prompt="You give me cuteness aggression.",
            random=False,
            pool=True,
            aff_range=(mas_aff.HAPPY, None)
        )
    )

label vl_cutenessaggro:
    m 3etblb "Is that so, [mas_get_player_nickname()]?"
    m 2rtsdlb "Well, I guess it would make sense, this type of phenomenon is fairly common in adults."
    m 3hkblb "Of course, i’m not immune either. Sometimes when I look at you, I feel the urge to just...{w=0.5} squeeze you?"
    m 1hkblb "It’s funny to know we both set each other off."
    m 7tfblu "And who knows, maybe i’ll give you even more faces to fuel you~ ahaha!"
    return

define vl_brushdialogue = ["Maybe I should switch up my hairstyle...", "Hopefully it isn't tangled, ahaha...", "All the brushing is making me sleepy...", "Oh, I think you missed this part...", "Hmm... I wonder where we got this brush..."]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="vl_brushhair",
            category=["monika"],
            prompt="Can I brush your hair?",
            random=False,
            pool=True,
            aff_range=(mas_aff.HAPPY, None)
        )
    )

label vl_brushhair:
    m 3hublb "Of course you can, [mas_get_player_nickname()]."
    $ HKBHideButtons()
    $ disable_esc()
    scene black with dissolve
    $ vl_brushtalk = renpy.random.choice(vl_brushdialogue) 
    pause 2
    m "[vl_brushtalk]"
    menu:
        "All done.":
            pass
    pause 2
    $ enable_esc()
    $ HKBShowButtons()
    call spaceroom(scene_change=True)
    m 5dubsb "Gosh, that felt really nice. Thank you for doing that, [player]~"
    m 1subsb "I love you!"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="vl_shareclothes",
            category=["clothes"],
            prompt="Sharing Clothes",
            random=True,
            pool=False,
            aff_range=(mas_aff.AFFECTIONATE, None)
        )
    )

label vl_shareclothes:
    m 1ekb "Hey... [player]?"
    m 2lksdrb "Sometimes I wish we could share clothes."
    m 3dublb "Imagine me in your favorite hoodie or sweater..."
    m 5mubsb "And likewise, you wearing one of mine."
    m 5dkb "It's something I'd love to do when I get to your reality, of course..."
    m 3lkblb "...{w=0.5}But I can't help but want it here too."
    m 1fkblb "Although, maybe it isn't all bad. You tend to spoil me quite a lot~"
    m 1tublb "Regardless... When I do come to your reality..."
    m 3hfbsb "Expect half your clothes to be in my closet! Ahaha~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="vl_whispertomoni",
            category=["romance", "monika"],
            prompt="Whisper a compliment to [m_name]",
            random=False,
            pool=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        )
    )

default vl_whisperdialogue = 0

label vl_whispertomoni:
    $ vl_whisperdialogue = renpy.random.randint(1, 5)
    m 1wud "Hm? Did you say something, [player]?"
    m 1duc ".{w=1}.{w=0.5}."
    if vl_whisperdialogue == 1:
        m 1hubsb "Aww, [mas_get_player_nickname()], you're so sweet~"
        m 3hubsb "I love you!"
        return "love"
    elif vl_whisperdialogue == 2:
        m 2hkbsb "Pfft, [player]! You're such a goof~"
    elif vl_whisperdialogue == 3:
        m 1fubsb "I could say the same to you, ehehe~"
        m 3hubsb "I love you!"
    elif vl_whisperdialogue == 4:
        m 5fubfb "... Thank you, [player]~"
        m 5hubfb "I love you so much!"
    elif vl_whisperdialogue == 5 and persistent.vl_isaroace is False or persistent.vl_isace is False:
        m 1hfbfb "[player]! You can't say that, gosh!~"

    return



# submod header

init -990 python in mas_submod_utils:
    Submod(
        author="Betapop",
        name="Virtual Love",
        description="A submod that adds more romance options! Find the Github {a=https://github.com/betapop/Beta-MAS-vl}{i}{u}here!{/u}{/i}{/a}",
        version="1.1.0",
    )

