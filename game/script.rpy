# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.
screen info:
    text _("HP: " + str(int(hero.hp)) + "%") pos(50, 250) size 36 color "#00fd" outlines [(2, "#fff8", 0, 0)]
    text _("Damage: " + str(int(hero.dmg))) pos(50, 300) size 36 color "#00fd" outlines [(2, "#fff8", 0, 0)]
    text _("Armor: " + str(int(hero.armor))) pos(50, 350) size 36 color "#00fd" outlines [(2, "#fff8", 0, 0)]
    text ("HP: " + str(int(monster.hp)) + "%") pos(1500, 300) size 36 color "#f00d" outlines [(2, "#fff8", 0, 0)]
    text ("Damage: " + str(int(monster.dmg))) pos(1500, 350) size 36 color "#f00d" outlines [(2, "#fff8", 0, 0)]
    text _("Armor: " + str(int(monster.armor))) pos(1500, 400) size 36 color "#f00d" outlines [(2, "#fff8", 0, 0)]
screen info_hero:
    text _("HP: " + str(int(hero.hp)) + "%") pos(50, 250) size 36 color "#00fd" outlines [(2, "#fff8", 0, 0)]
    text _("Damage: " + str(int(hero.dmg))) pos(50, 300) size 36 color "#00fd" outlines [(2, "#fff8", 0, 0)]
    text _("Armor: " + str(int(hero.armor))) pos(50, 350) size 36 color "#00fd" outlines [(2, "#fff8", 0, 0)]

label start:

    #init block
    python:
        from player import Player
        from enemy import Enemy
        import random
        hero = Player()

    "ВСЕМ ПРИВЕТ В ЭТОМ ЧАТИКЕ"
    jump path_choose

    # This ends the game.
    label endgame:
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
        $rand = 0
        if rand == 0:
            show scelet at right
            python:
                #scelet
                monster = Enemy(30, 10, 5, [1.0, 1.5, 1.0])
                monster.messages[0] = "Вы втебали скелеут в черепуху, лол"
                monster.messages[1] = "Минус ребра у скелета, лол"
                monster.messages[2] = "Минус ноги, лол"
        elif rand == 1:
            jump monster1
        elif rand == 2:
            jump monster2
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
        show screen info_hero
        "we a getting treasures!"
        jump path_choose
