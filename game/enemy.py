DAMAGE_MULTIPLAYER = [1.0, 1.0, 1.0]
MONSTER_DAMAGE = 5
MONSTER_HP = 50
MONSTER_ARMOR = 10

class Enemy:

    messages = ["", "", ""]
    def __init__(self, hp, dmg, armor, dmg_m):
        self.hp = hp
        self.dmg = dmg
        self.armor = armor
        self.dmg_m = dmg_m


    def get_damage(self, damage, body_part):
        damage = damage*self.dmg_m[body_part]
        self.armor -= damage
        if self.armor < 0 :
            self.hp += self.armor
            self.armor = 0
