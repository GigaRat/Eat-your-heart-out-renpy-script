# Declare characters used by this game.
define k = Character(_("Kyou"), color="#803724")
define j = Character(_("Jihoon"), color="#c8c8ff")
define r = Character(_("Rinnie"), color="#c8c8ff")
define mc = Character(_("Niko"))

# The game starts here.
label start:

    # Start by playing some music.
    # play music "audio/love_start_opening.mp3"

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

    show kyou n

    k "Are you just going to stand there or can I grab my snack?"

    mc "Oooohhh… yeah that is only if you ask nicely"

    k "...."

    menu:
        "...":
            $ kyou_affection =+10
            jump .Beg
            #10 points
        "Okay, fine....you're no fun":
            $ kyou_affection =+5
            jump .Smirk
            #5 points
        "Did i make you speechless?":
            $ kyou_affection =+15
            jump .Blushes
            #15 points


label .Beg:

    "Oh sir, would you be ever so kind as to step aside?"
    jump Grocery_end

label .Smirk:
    
    "That was a little too easy. I was expecting a little more fight out of you."
    jump Grocery_end

label .Blushes:
    
    "Kyou blushes, picks you up and pushes you aside. Not too much of a challenge there"
    jump Grocery_end


label Grocery_end:

    k "Collects his snack and pats you on the head. See you later pet name"

    mc "pet name?!?"

    mc "Phew… my heart is pounding...if that lasted any longer i would have started barking"

    "Anyways..."

    "I guess I should wait to figure out what I am going to bake for white day."

    "I need to hang on to this money just in case… and wait until i have made my decision on who to bake for."

    "Like i said, there aarrree a couple more that have caught my eye…"

    #this marks the end of scene 1 for k.

    #splashscreen

    #scene 2 starts here.

label s2:

    #Start scene with dorm music 
    #play music "dorm.mp3"

    scene bg dorm
    with fade

    #MC is narrating this portion
    "I’ve been really busy between classes at the university and having to be the dorm's RA. But I can’t stop thinking about White day since it’s so close now…"

    "I’ve never really had to “woo” somebody since I only came out my last year of high school…"

    "I just wonder what kind of dessert screams \“I want to hold your hand in the gay ki-\”"

    "Wait, is that Jihoon reading a book over there? Speaking of dessert.."

    #play music "audio/jihoonloop.mp3"
    show jihoon n

    j "Oh, Niko... I've been looking for you."

    mc "Let me guess. You’re locked out again because you were so engrossed in reading?"

    show jihoon s

    j "....Would you be able to open it up for free this time? I know I said I wouldn’t forget anymore, but-"

    mc "Oookay but you know I can't do it for free. The fee this time will have to be heftier considering last time it was only 5 dollars."

    #show jihoon a

    j "That seems only fair..What is the fee this time Niko?"

    "Why did he say my name like that..."

    menu: 
        "...":
            jump jihoon_annoyed

        "Welllll…..how about a kiss?":
            jump jihoon_annoyed

label jihoon_annoyed:

    j "Would you stop joking around? I have to get back to my dorm soon…?"

    menu:
        "Okay, okay. I’ll open it for free. Just know next time there will be higher stakes":
            jump .option_1
            #2 points

        "What? Afraid to kiss another boyyyy":
            jump .option_2
            #20 points

label .option_1:

    #show Jihoon sur

    j "Thank you. And I promise it won’t happen again…for real this time."

    mc "Ohh you know, I do what I can as the RA."

    " I should probably be careful with pushing him around too much. I would hate to lead him on."

    j "Although I am not typically one to encourage others to go against the rules, I appreciate you turning a blind eye..If there's anything I can do for you, please tell me"
    
    "ANYTHING? Come ooonnnn, you’re just *asking* me to give you a big smooch right here!"
    
    mc "It’s okay! Just make sure it doesn’t happen again, or else I *really* can’t give you any more free passes. In any case, you know where I’ll be."

    jump s3
    
label .option_2:

    j "..I am considering sleeping outside if this continues."

    "He’s just SO cute when he blushes- I find it hard to resist teasing him."

    mc "Okay okaaay! I’ll open it this time for free. Just know that next time, I’ll assume you’re just trying to get me into your room."

    #show Jihoon n

    j "....Well, while we’re on that subject. There’s a book I've been reading that I’m certain you would enjoy."

    j "If you come by my room later I might be done reading it, and you could borrow it if you would like?"

    "Wow, he is SO cute I could burst into flames! He’s screening a book to make sure I would like it?!! HOW CUTE!!"

    mc "Is this just an excuse to get me in your room, Jihoon?"

    #show Jihoon s

    j "..."

    "Wait…is he into me!?"

    mc "“I think it's sweet that you are considering sharing a book with me, Jihoon. I trust your judgment!"

    mc "…Just make sure it’s not a period piece."

    #show Jihoon smile

    j "Okay Niko...a period piece it is."

    mc "Jihoon, as cute as you are I am not readi-"

    j "I’m trying to create banter, Niko."

    "What. A. Dork"

    mc "You…I'll come by later to pick up the book. And don’t even THINK about handing me a period piece or there will be consequences!"

    #show j shy

    j "I’ll accept my punishment.."

    "PUNISHMENT?! WHAT DOES HE THINK THIS IS...."

    #this marks the end of scene 2

    #splashscreen

    #scene 3 starts here

label s3:

    #play slow night time music

    scene bg dorm_night
    with fade

    "It’s really hard to decide between those two. I have no idea how I’m going to pick, they’re just both SO cute!!"

    "I have a lot to think about tomorrow, but for now I should just focus on getting some sleep..."

    #have screen shake at this part
    "??????" "WOOOOOOOOOOOOOOOOOOOO!!!!!!"

    "?????????" "yEAHHHHH GET HIMMMMM"

    "Ugh, I guess I have to go see what that yelling is…"

    #transition to outside dorm

    scene bg school_courtyard
    with fade

    mc "Sorry, you guys need to find somewhere else t-"

    #screen shake
    r "RRRRAH!!!!!!!!!!"

    show rinnie n

    r "Oh, sorry! I thought you were one of my teammates!"

    mc "It…it’s okay. Can you get off of me?"

    r "We have a new tournament coming up, so we were out here practicing! Here, I’ll show you!"

    mc "Hold on, I think I got it the first time. No need for another demonstration!"
 

