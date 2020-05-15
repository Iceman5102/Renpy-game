HERO_MAX_HP = 100
HERO_DAMAGE = 10
HERO_ARMOR = 30
HERO_LVL = 0
HERO_LVL_COST = [100, 200, 300, 400, 500]
HP_PER_POTION = 30
ITEM_MAX_HP = [5, 10, 15, 20]
ITEM_HP = [10, 20, 30, 40]
ITEM_ARMOR = [10, 20, 30, 40]
ITEM_DAMAGE = [1,2,3,4]
ITEM_EXP = [25, 50, 75, 100]
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
            
    def item(self, rarity, type):
        if (type == "max_hp"):
            if (rarity == "common"):
                self.max_hp += ITEM_MAX_HP[0]
                self.add_hp(ITEM_MAX_HP[0])
            if (rarity == "rare"):
                 self.max_hp += ITEM_MAX_HP[1]
                 self.add_hp(ITEM_MAX_HP[1])
            if (rarity == "epic"):
                 self.max_hp += ITEM_MAX_HP[2]
                 self.add_hp(ITEM_MAX_HP[2])
            if (rarity == "legendary"):
                 self.max_hp += ITEM_MAX_HP[3]
                 self.add_hp(ITEM_MAX_HP[3])
        if (type == "hp"):
            if (rarity == "common"):
               self.add_hp(ITEM_HP[0])
            if (rarity == "rare"):
                self.add_hp(ITEM_HP[1]) 
            if (rarity == "epic"):
                self.add_hp(ITEM_HP[2])
            if (rarity == "legendary"):
                self.add_hp(ITEM_HP[3])
        if (type == "armor"):
            if (rarity == "common"):
                self.armor += ITEM_ARMOR[0]
            if (rarity == "rare"):
                 self.armor += ITEM_ARMOR[1]
            if (rarity == "epic"):
                 self.armor += ITEM_ARMOR[2]
            if (rarity == "legendary"):
                 self.armor += ITEM_ARMOR[3]
        if (type == "damage"):
            if (rarity == "common"):
                self.dmg += ITEM_DAMAGE[0]
            if (rarity == "rare"):
                 self.dmg += ITEM_DAMAGE[1]
            if (rarity == "epic"):
                 self.dmg += ITEM_DAMAGE[2]
            if (rarity == "legendary"):
                 self.dmg += ITEM_DAMAGE[3]
        if (type == "exp"):
            if (rarity == "common"):
                self.add_exp(ITEM_EXP[0])
            if (rarity == "rare"):
                 self.add_exp(ITEM_EXP[1])
            if (rarity == "epic"):
                 self.add_exp(ITEM_EXP[2])
            if (rarity == "legendary"):
                 self.add_exp(ITEM_EXP[3])