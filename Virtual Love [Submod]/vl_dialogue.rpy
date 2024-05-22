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
    m 1kublb "I’m sorry, your beauty was too distracting~"
    m 3hublb "I can’t help but smile when i’m around you!"
    m 2fubsb "You’re the best thing that happened to me, after all.{nw}"
    $ _history_list.pop()
    menu:
        m "You’re the best thing that happened to me, after all.{fast}"

        "I smile when i’m around you too.":
            m 4hubsb "Thank you, i’m glad I can make you so happy!"
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
                return "love"

            "Nose.":
                m 3hkbsb "Ah— [player]! That tickles~"
                m 4tkbsb "Thanks for the kiss, ehehe."
                return "love"
        
            "Neck.":
                m 2tsbsb "Oh~ The neck, huh?"
                m 2msbfb "Well, I can’t say I didn’t enjoy it."
                m 2ktbfb "Want to go again?"
                m 3hubfb "Ahaha, just teasing!"
                return "love"
        
            "Hand.":
                m 1sublb "I feel so royal~ hehe."
                m 3hubsb "Thank you, my kind knight!"
                return "love"
        
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
            return "love"

        elif ev.shown_count == 1:
            m 5hkbfb "Im never ready!~"
            return "love"

        else:
            m 1tsbfb "Pff, again, [player]~?"
            return "love"

    else:
        "I don't think she's ready for that yet... "
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_vl_checkin",
            category=["us"],
            prompt="I'm sorry I don't check in as often.",
            random=False,
            pool=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )


label monika_vl_checkin:
    m 1hub "Don’t worry about that too much, [player]."
    m 3rkb "Obviously, I do miss you when you’re gone..."
    m 4hksdlb "But I know you have things to do, and life to live."
    m 3tksdlb "And I don’t want to stop you from experiencing that."
    m 3hub "All I ask is that if it’s for a while, you tell me, okay?"
    m 5kublb "I can wait. And i’ll be glad to wait if I know i’ll see your cute face when you’re back!"

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
    m 3hubfb "I love you so much… and let’s continue on with the day!"

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
    m 3hublb "I’d love you just the way you are~ and nothing will change that!"

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

return "love"

default persistent._mas_pm_isaroace = False
default persistent._mas_pm_inqpr = False


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_vl_acespec",
            category=['romance', 'you'],
            prompt="[m_name], I’m asexual and or aromantic.",
            random=False,
            pool=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )


label monika_vl_acespec:
    $ ev = mas_getEV("monika_vl_acespec")
    if ev.shown_count == 0:
        m 1etb "Oh! Do you mind clarifying a bit more, [player]?{nw}"
        $ _history_list.pop()
        menu:
            m "Oh! Do you mind clarifying a bit more, [player]?{fast}"

            "I’m just asexual.":
                jump vl_acespec_contin
                

            "I’m just aromantic.":
                jump vl_acespec_contin
                

            "I’m aroace.":
                jump vl_acespec_contin
    else:
        m 3hkblb "I already know~"
        return
                

label vl_acespec_contin:
    m 1dkb "I see… Well, firstly, thank you for feeling comfortable enough to tell me."
    m 3hkb "And of course, I fully support you. Nothing will ever change that."
    m 2gksdlb "Though, that does change our relationship a little, huh?"
    m 2dksdld "I’m sorry if i’ve ever made you uncomfortable. I wish I would’ve known sooner..."
    m 4fkb "But know that I know, I’ll try to be more mindful."
    m 3hkblb "And this information doesn’t shake the love I have for you, [mas_get_player_nickname()]."
    m 5fkblb "Romantic or not, I cherish you just as much."
    $ persistent._mas_pm_isaroace = True
    if mas_isMoniEnamored(higher=True):
        m 5mkblb "And you’ve stuck around so long, i’m sure you feel the same."
        m 3hublb "Right! Let’s continue with our day, shall we?~"
    else:
        m 3hublb "Right! Let’s continue with our day, shall we?~"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_vl_qpr",
            category=['romance', 'you'],
            prompt="Hey [m_name], can we have a queerplatonic relationship?",
            pool=True,
            random=False,
            aff_range=(mas_aff.NORMAL, None),
        )
    )

label monika_vl_qpr:
    $ ev = mas_getEV("monika_vl_qpr")
    if ev.shown_count == 0:
        m 1wublb "A queerplatonic relationship? I’m open to the idea! I just don’t know much about them.{nw}"
        $ _history_list.pop()
        menu:
            m "A queerplatonic relationship? I’m open to the idea! I just don’t know much about them.{fast}"

            "They’re a type of relationship that’s not romantic but not just friendship, either.":
                m 3hublb "That makes sense! Thank you for telling me."
                m 5hublb "If that’s what makes you the most comfortable [mas_get_player_nickname()], of course i’m happy to."
                m 3hublb "And i’m excited to explore this with you~"
                m 2eublb "Just let me know if you ever want to go back to a traditional relationship, alright?"
                $ persistent._mas_pm_inqpr = True
                return
    else:
        if persistent._mas_pm_inqpr is True:
            m 3hkblb "We're already in one, silly!"
        elif persistent._mas_pm_inqpr is False:
            $ persistent._mas_pm_inqpr = True
            m 1eub "You want to go back into a queerplatonic relationship? Alright!"
        else:
            m 2gksdlb "There might be an error, I can't tell the status of our relationship. Sorry, [player]!"
        return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_vl_tradship",
            category=['romance', 'you'],
            prompt="Hey [m_name], can we have a traditional relationship?",
            pool=True,
            random=False,
            aff_range=(mas_aff.NORMAL, None),
        )
    )

label monika_vl_tradship:
    if persistent._mas_pm_inqpr is False:
        m 3hkblb "We're already in one, silly!"
    elif persistent._mas_pm_inqpr is True:
        $ persistent._mas_pm_inqpr = False
        m 1eub "You want to go back into a traditional relationship? Alright!"
    else:
        m 2gksdlb "There might be an error, I can't tell the status of our relationship. Sorry, [player]!"
    return