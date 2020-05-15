# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

screen info:
    text _("HP: " + str(int(hero.hp)) + "%/" +  str(int(hero.max_hp)) + "%" ) pos(50, 250) size 36 color "#00fd" outlines [(2, "#fff8", 0, 0)]
    text _("Damage: " + str(int(hero.dmg))) pos(50, 300) size 36 color "#00fd" outlines [(2, "#fff8", 0, 0)]
    text _("Armor: " + str(int(hero.armor))) pos(50, 350) size 36 color "#00fd" outlines [(2, "#fff8", 0, 0)]
    text ("HP: " + str(int(monster.hp)) + "%") pos(1500, 300) size 36 color "#f00d" outlines [(2, "#fff8", 0, 0)]
    text ("Damage: " + str(int(monster.dmg))) pos(1500, 350) size 36 color "#f00d" outlines [(2, "#fff8", 0, 0)]
    text _("Armor: " + str(int(monster.armor))) pos(1500, 400) size 36 color "#f00d" outlines [(2, "#fff8", 0, 0)]
screen info_hero:
    text _("HP: " + str(int(hero.hp)) + "%/" +  str(int(hero.max_hp)) + "%" ) pos(50, 250) size 36 color "#00fd" outlines [(2, "#fff8", 0, 0)]
    text _("Damage: " + str(int(hero.dmg))) pos(50, 300) size 36 color "#00fd" outlines [(2, "#fff8", 0, 0)]
    text _("Armor: " + str(int(hero.armor))) pos(50, 350) size 36 color "#00fd" outlines [(2, "#fff8", 0, 0)]
screen name:
    text _(NAMES[i, 0]+ ": " + str(NAMES[i,3])) pos (NAMES[i, 1], NAMES[i, 2]) size 40 color "00fd"
label start:

    #init block
    python:
        from player import Player
        from enemy import Enemy
        import random
        hero = Player()

    jump path_choose

    # This ends the game.
    label endgame:
        python:
            NAMES = [ ["1", 300, 300, 1500], ["2", 300, 350, 1000],["3", 300, 400, 100], ["4", 300, 350, 50] ]
            name = renpy.input("Введите имя")
        
        $i = 0
        while i < 4:
            show screen name
            $i += 1
        "Щёлкните для конца игры"
    return

    #choose path, fight or treasure
    label path_choose:
        scene bg two_doors with dissolve
        show hero at left
        show screen info_hero
        "choose a door"
        menu:
            "left door":
                "entering left door"
            "right door":
                "entering right door"
        $rand = random.randint(0, 2)
        if( rand == 1 ):
            jump treasure
        else:
            jump fight

    #main fight
    label fight:
        scene bg fight with dissolve
        "we a fighting right now"
        #$rand = random.randint(0, 9)
        $rand = 1
        if rand == 0:
            show scelet at right
            python:
                #scelet
                monster = Enemy(30, 10, 5, [1.0, 1.5, 1.0])
                monster.messages[0] = "Вы втебали скелеут в черепуху, лол"
                monster.messages[1] = "Минус ребра у скелета, лол"
                monster.messages[2] = "Минус ноги, лол"
        elif rand == 1:
            show monster1 at right
            python:
                monster = Enemy(50, 150, 15, [1.4, 1.2, 1.2])
                monster.messages[0] = "Вы ударили мага в голову, лол"
                monster.messages[1] = "Минус ребра у мага, лол"
                monster.messages[2] = "Минус ноги, лол"
        elif rand == 2:
            show monster2 at right
            python:
                monster = Enemy(100, 13, 15, [1.4, 1.2, 1.2])
                monster.messages[0] = "Вы ударили мага в голову, лол"
                monster.messages[1] = "Минус ребра у мага, лол"
                monster.messages[2] = "Минус ноги, лол"
        elif rand == 3:
            jump monster3
        elif rand == 4:
            jump monster4
        elif rand == 5:
            jump monster5
        elif rand == 6:
            jump monster6
        elif rand == 7:
            jump monster7
        elif rand == 8:
            jump monster8
        elif rand == 9:
            jump monster9


        while hero.hp > 0 and monster.hp > 0:
            label attack_choice:
                show screen info
                menu:
                    "Attack":
                        menu:
                            "attack head":
                                $hero.get_damage(monster.dmg)
                                $monster.get_damage(hero.dmg, 0)
                                "[monster.messages[0]]"
                            "attack body":
                                $hero.get_damage(monster.dmg)
                                $monster.get_damage(hero.dmg, 1)
                                "[monster.messages[1]]"
                            "attack legs":
                                $hero.get_damage(monster.dmg)
                                $monster.get_damage(hero.dmg, 2)
                                "[monster.messages[2]]"
                            "back":
                                jump attack_choice
                            "do nothink":
                                $hero.get_damage(monster.dmg)
                                "debug llol"
                    "Use Potion":
                        "?????"
                        $hero.add_hp(30)
                        $hero.get_damage(monster.dmg)

        label end_of_fight:
            if (hero.hp > 0) :
                #win words (+exp, lvlup?)
                "YOU WIN"
                hide screen info
                jump path_choose
            else:
                #loose => to the end of the game =)
                jump endgame

    #fight with monstr0
    label monster0:
        #put image of enemy
        "[rand]"
        jump endgame
        
    
    
    label treasure:
        scene bg treasure with dissolve
        
        $randtype = random.randint(0, 100)
        $rand = random.randint(0, 4)

    if (randtype < 40):
        show common circle_img:
            yalign .5 subpixel True
            xalign .5 subpixel True
            zoom 0.8
        if (rand == 0):
            $hero.item("common", "max_hp")
            show oranges_img:
                yalign .5 subpixel True
                xalign .5 subpixel True
                zoom 1.5
        elif (rand==1):
            $hero.item("common", "hp")
            show first aid_img:
                yalign .5 subpixel True
                xalign .5 subpixel True
                zoom 0.8
        elif (rand==2):
            $hero.item("common", "armor")
            show armor_img:
                yalign .5 subpixel True
                xalign .5 subpixel True
                zoom 1.0
        elif (rand==3):
            $hero.item("common", "damage")
            show axe_img:
                yalign .5 subpixel True
                xalign .5 subpixel True
                zoom 0.9
        elif (rand==4):
            $hero.item("common", "exp")
            show exp_potion_img:
                yalign .49 subpixel True
                xalign .49 subpixel True
                zoom 4.0
                
    elif (randtype >= 40 and randtype < 70):
        show rare circle_img:
            yalign .5 subpixel True
            xalign .5 subpixel True
            zoom 0.8
        if (rand == 0):
            $hero.item("rare", "max_hp")
            show oranges_img:
                yalign .5 subpixel True
                xalign .5 subpixel True
                zoom 1.5
        elif (rand==1):
            $hero.item("rare", "hp")
            show first aid_img:
                yalign .5 subpixel True
                xalign .5 subpixel True
                zoom 0.8
        elif (rand==2):
            $hero.item("rare", "armor")
            show armor_img:
                yalign .5 subpixel True
                xalign .5 subpixel True
                zoom 1.0
        elif (rand==3):
            $hero.item("rare", "damage")
            show axe_img:
                yalign .5 subpixel True
                xalign .5 subpixel True
                zoom 0.9
        elif (rand==4):
            $hero.item("rare", "exp")
            show exp_potion_img:
                yalign .49 subpixel True
                xalign .49 subpixel True
                zoom 4.0
                
    elif (randtype >= 70 and randtype < 90):
        show epic circle_img:
            yalign .5 subpixel True
            xalign .5 subpixel True
            zoom 0.8
        if (rand == 0):
            $hero.item("epic", "max_hp")
            show oranges_img:
                yalign .5 subpixel True
                xalign .5 subpixel True
                zoom 1.5
        elif (rand==1):
            $hero.item("epic", "hp")
            show first aid_img:
                yalign .5 subpixel True
                xalign .5 subpixel True
                zoom 0.8
        elif (rand==2):
            $hero.item("epic", "armor")
            show armor_img:
                yalign .5 subpixel True
                xalign .5 subpixel True
                zoom 1.0
        elif (rand==3):
            $hero.item("epic", "damage")
            show axe_img:
                yalign .5 subpixel True
                xalign .5 subpixel True
                zoom 0.9
        elif (rand==4):
            $hero.item("epic", "exp")
            show exp_potion_img:
                yalign .49 subpixel True
                xalign .49 subpixel True
                zoom 4.0
                
    elif (randtype >= 90):
        show legendary circle_img:
            yalign .5 subpixel True
            xalign .5 subpixel True
            zoom 0.8
        if (rand == 0):
            $hero.item("legendary", "max_hp")
            show oranges_img:
                yalign .5 subpixel True
                xalign .5 subpixel True
                zoom 1.5
        elif (rand==1):
            $hero.item("legendary", "hp")
            show first aid_img:
                yalign .5 subpixel True
                xalign .5 subpixel True
                zoom 0.8
        elif (rand==2):
            $hero.item("legendary", "armor")
            show armor_img:
                yalign .5 subpixel True
                xalign .5 subpixel True
                zoom 1.0
        elif (rand==3):
            $hero.item("legendary", "damage")
            show axe_img:
                yalign .5 subpixel True
                xalign .5 subpixel True
                zoom 0.9
        elif (rand==4):
            $hero.item("legendary", "exp")
            show exp_potion_img:
                yalign .49 subpixel True
                xalign .49 subpixel True
                zoom 4.0
                
    show screen info_hero
    "we a getting treasures!"
    jump path_choose
