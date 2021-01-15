class Spell:

    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    def change_damage(self, new_damage):
        self.damage = new_damage

    def change_mana_cost(self, new_mana_cost):
        self.mana_cost = new_mana_cost

    def return_spell_info(self):
        return f"\033[32m{self.name}\033[0m - Damage: {self.damage}, Mana cost: {self.mana_cost}"


class Effect:

    def __init__(self, name, add_atk, add_dfs, time, applied=False):       # time - number of rounds
        self.name = name
        self.add_atk = add_atk
        self.add_dfs = add_dfs
        self.time = time + 1
        self.applied = applied

    def return_effect_info(self):
        return f"\033[32m{self.name}\033[0m - Additional damage: {self.add_atk}, Additional defense: {self.add_dfs}"