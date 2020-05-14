HERO_MAX_HP = 100
HERO_DAMAGE = 10
HERO_ARMOR = 30
HERO_LVL = 0
HERO_LVL_COST = [100, 200, 300, 400, 500]
HP_PER_POTION = 30

class Player:
    max_hp = HERO_MAX_HP
    hp = HERO_MAX_HP
    armor = HERO_ARMOR
    dmg = HERO_DAMAGE
    lvl = HERO_LVL
    exp = 0
    potion = 0
    def add_hp(self, heal):
        self.hp += heal
        if (self.hp > self.max_hp):
            self.hp = self.max_hp

    def add_exp(self, exp):
        self.exp += exp
        lvl_exp = HERO_LVL_COST[self.lvl]
        while (self.exp > lvl_exp):
            self.lvlup(self)
            self.exp = exp - lvl_exp

    def lvl_up(self):
        self.lvl =+ 1

    def get_damage(self, damage):
        if (self.armor >= damage):
            self.armor -=damage
        else:
            self.hp -= (damage - self.armor)
            self.armor = 0
