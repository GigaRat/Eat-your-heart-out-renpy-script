# Declare characters used by this game.
define k = Character(_("kyou"), color="#c8ffc8")
define m = Character(_("Masa"), color="#c8c8ff")
define r = Character(_("Rinnie"), color="#c8c8ff")
define mc = Character(_("Me"))


# The game starts here.
label start:

    # Start by playing some music.
    play music "audio/love_start_opening.mp3"

    scene bg groceryaisle
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


    ???? "Hey..." 
    
    mc "speaking of sweet selections.. Here comes one of them" 
    
    k "Are you just going to stand there or can I grab my snack?"

    mc "Oooohhh… yeah that is only if you ask nicely"

    K "..."

    menu introK:
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

label Smirk

label Blushes: 

        


