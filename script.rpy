# Declare characters used by this game.
define k = Character(_("kyou"), color="#c8ffc8")
define m = Character(_("Masa"), color="#c8c8ff")
define r = Character(_("Rinnie"), color="#c8c8ff")
define mc = Character(_("Me"))


# The game starts here.
label start:

    # Start by playing some music.
    # play music "love_start_opening"

    scene bg grocery
    with fade

    mc "White day is coming up...."

    mc "I transferred to *all boys school college* a couple months ago and have been staying the dorms as an RA."

    mc "I’ve come so far along at this school and i don’t have a boyfriend yet!…"

    mc "There are a lot of options to consider \(for some reason…\)."

    mc "but I guess you could say I have a sweet tooth for a select few…"

    mc "I just don't know what I am going to make..."

    mc "I think I should get to know them first before I spend a ton of ingredients."

    mc "I do have to survive on my \$50\ until next we-"

#First decision for player towards Kyou.


    "????" "Hey..."

    mc "speaking of sweet selections.. Here comes one of them"

    #Show k

    k "Are you just going to stand there or can I grab my snack?"

    mc "Oooohhh… yeah that is only if you ask nicely"

    k "..."

    menu:
        "....":
            jump Beg
            #10 points
        "Okay, fine....you're no fun":
            jump Smirk
            #5 points
        "Did i make you speechless?":
            jump Blushes
            #15 points


label Beg:
    $ beg_points = 10
    "oh sir, would you be ever so kind as to step aside?"
    jump Grocery_end

label Smirk:
    $ smirk_points = 5
    "that was TOO easy pet name"
    jump Grocery_end

label Blushes:
    $ blush_points = 15
    "Kyou blushes, picks you up and pushes you aside. Not too much of a challenge there pet name"
    jump Grocery_end


label Grocery_end:

    k "collects his snack and pats you on the head. See you later pet name"

    mc "pet name?!?"

    mc "Phew… my heart is pounding...if that lasted any longer i would have started barking"

    "Anyways..."

    "I guess I should wait to figure out what I am going to bake for white day."

    "I need to hang on to this money just in case… and wait until i have made my decision on who to bake for."

    "Like i said, there aarrree a couple more that have caught my eye…"

    return

    #this marks the end of scene 1 for k.

    #splashscreen

    #scene 2 starts here.

