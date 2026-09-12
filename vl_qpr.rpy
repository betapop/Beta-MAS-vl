# i had to rewrite all of this since that power outage... should be fine
# now though lol

default persistent.vl_isaroace = False
default persistent.vl_isaro = False
default persistent.vl_isace = False

default persistent.vl_moniace = False

default persistent.vl_inqpr = False
default persistent.vl_seenqprspeech = False

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="vl_acespec",
            category=['romance', 'you'],
            prompt="[m_name], I'm asexual and/or aromantic.",
            random=False,
            pool=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )


label vl_acespec:
    $ ev = mas_getEV("vl_acespec")
    if ev.shown_count == 0:
        m 1etb "Oh! Do you mind clarifying a bit more, [player]?"
        jump vl_acespec_loop_1

    else:
        m 3hkblb "I already know~"
        m 1wud "Unless something has changed?"
        jump vl_acespec_loop_2

                
label vl_acespec_loop_1:
    menu:
        "I'm just asexual." if persistent.vl_isace is False:
            $ persistent.vl_isace = True
            jump vl_acespec_contin
            

        "I'm just aromantic." if persistent.vl_isaro is False:
            $ persistent.vl_isaro = True
            jump vl_acespec_contin
            

        "I'm aroace." if persistent.vl_isaroace is False:
            $ persistent.vl_isaroace = True
            jump vl_acespec_contin

        "Nevermind.":
            m 2eub "Oh, alright! Well, if something changes, you can always let me know."
            return

label vl_acespec_loop_2:
    menu:
        "I'm just asexual." if persistent.vl_isace is False:
            $ persistent.vl_isaroace = False
            $ persistent.vl_isaro = False
            $ persistent.vl_isace = True
            m 3hub "Alright! Thats fine with me, as long as you're comfortable~"
            m 2eub "You're always free to explore your sexual identity, of course."
            m 1hub "Let me know if it changes again!"
            return
            

        "I'm just aromantic." if persistent.vl_isaro is False:
            $ persistent.vl_isaroace = False
            $ persistent.vl_isace = False
            $ persistent.vl_isaro = True
            m 3hub "Alright! Thats fine with me, as long as you're comfortable~"
            m 2eub "You're always free to explore your sexual identity, of course."
            m 1hub "Let me know if it changes again!"
            return
            

        "I'm aroace." if persistent.vl_isaroace is False:
            $ persistent.vl_isaro = False
            $ persistent.vl_isace = False
            $ persistent.vl_isaroace = True
            m 3hub "Alright! Thats fine with me, as long as you're comfortable~"
            m 2eub "You're always free to explore your sexual identity, of course."
            m 1hub "Let me know if it changes again!"
            return

        "I'm Allosexual." if persistent.vl_isaroace is True or persistent.vl_isaro is True or persistent.vl_isace is True:
            $ persistent.vl_isaroace = False
            $ persistent.vl_isaro = False
            $ persistent.vl_isace = False
            m 3hub "Alright! Thats fine with me, as long as you're comfortable~"
            m 2eub "You're always free to explore your sexual identity, of course."
            m 1hub "Let me know if it changes again!"
            return

        "Nothing changed.":
            m 2eub "Alright~ Let me know if it does!"
            return


label vl_acespec_contin:
    m 1dkb "I see...{w=0.5} Well, firstly, thank you for feeling comfortable enough to tell me."
    m 3hkb "And of course, I fully support you. Nothing will ever change that, [player]."
    m 2gksdlb "Though, that does change our relationship a little, huh?"
    m 2dksdld "I'm sorry if I've ever made you uncomfortable. I wish I would’ve known sooner..."
    m 4fkb "But know that I know, I'll try to be more mindful."
    m 3hkblb "And this information doesn’t shake the love I have for you, [mas_get_player_nickname()]."
    
    if persistent.vl_isaro is True:
        m 5fkblb "Romantic or not, I cherish you just as much."
    elif persistent.vl_isaroace is True:
        m 5fkblb "Even if it's not romantic or platonic, I cherish you just as much."
    else:
        m 5fkblb "Sexual or not, I cherish you just as much."
    if mas_isMoniEnamored(higher=True):
        m 5mkblb "And you’ve stuck around so long, I'm sure you feel the same."
    else:
        pass
    
    m "Thank you for telling me again, [player]. It might take a while for me to adjust, but I really apperiate that you told me."
    m "And if I ever bring up something that's too uncomfortable for you, you can always press X to let me know, okay?"
    m "I love you so much, [mas_get_player_nickname()]. Nothing will ever change that."
    m 3hublb "Right! Let’s continue with our day, shall we?~"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="vl_qpr",
            category=['romance', 'you', 'us'],
            prompt="Hey [m_name], can we change our type of relationship?",
            pool=True,
            random=False,
            aff_range=(mas_aff.NORMAL, None),
        )
    )

label vl_qpr:
    $ ev = mas_getEV("vl_qpr")
    if ev.shown_count == 0:
        m "Oh? What type of relationship, [player]?"
        jump vl_relationship_loop

    else:
        m "Oh, did you want to change it again?"
        menu:
            "Yeah. Can we have a...":
                jump vl_relationship_loop
        return

label vl_relationship_loop:
    menu:
        "A queerplatonic relationship." if persistent.vl_inqpr is False:
            $ persistent.vl_inqpr = True
            if persistent.vl_seenqprspeech is False:
                m 1wublb "A queerplatonic relationship? I'm open to the idea! I just don’t know much about them.{nw}"
                $ _history_list.pop()
                menu:
                    m "A queerplatonic relationship? I'm open to the idea! I just don’t know much about them.{fast}"

                    "They’re a type of relationship that’s not romantic but not just friendship, either.":
                        m 3hublb "That makes sense! Thank you for telling me."
                        m 5hublb "If that’s what makes you the most comfortable [mas_get_player_nickname()], of course I'm happy to."
                        m 3hublb "And I'm excited to explore this with you~"
                        m 2eublb "Just let me know if you ever want to go back to a traditional relationship, alright?"
                        $ persistent.vl_seenqprspeech = True
                        return
            else:
                $ persistent.vl_inqpr = True
                m 1eub "You want to go back into a queerplatonic relationship? Alright!"
                return

        "A traditional relationship." if persistent.vl_inqpr is True:
            $ persistent.vl_inqpr = False
            m 1eub "You want to go back into a traditional relationship? Alright!"
            return

        "Nevermind.":
            "Oh, alright. Feel free to ask again if you do want to!"
            return
