from die import *


class NotEnoughMana(Exception):
    pass


class Character:

    die6 = Die(6)

    def __init__(self, name, hp, atk, dfs):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.dfs = dfs

    @staticmethod
    def attack(atk_val, target):
        target.get_hit(atk_val)

    def get_hit(self, atk_val):
        curr_hp = self.hp
        atk_val = abs(atk_val - self.dfs) + self.die6.roll()
        self.hp -= atk_val
        print("\033[0:31m{} got hit for {} points\033[0m".format(self.name, curr_hp - max(0, self.hp)))

    def is_dead(self):
        if self.hp <= 0:
            return True
        else:
            return False


class Player(Character):
    def __init__(self, name, mp, hp, atk, dfs, available_spells=[], effects_on=[]):
        super().__init__(name, hp, atk, dfs)
        self.available_spells = available_spells
        self.effects_on = effects_on
        self.mp = mp
        self.full_mp = mp

    def apply_effects(self):        # TODO added
        for e in self.effects_on:
            e.time -= 1
            if not e.applied:
                self.atk += e.add_atk
                self.dfs += e.add_dfs
                e.applied = True
                print(f"\033[32mEffect {e.name} is now applied for {e.time} rounds\033[0m")
            if e.time == 0:
                self.atk -= e.add_atk
                self.dfs -= e.add_dfs
                self.effects_on.remove(e)
                print(f"\033[32mEffect {e.name} has ended\033[0m")

    def say_hello(self):
        return "My name is " + self.name

    def use_spell(self, spell):
        # spell = {
        #     'fireball': [30, 50],
        #     'icicle': [25, 40],
        #     'default': [self.atk, 0]
        # }.get(spell, [self.atk, 0])
        if self.mp >= spell.mana_cost:
            self.mp -= spell.mana_cost
            return spell.damage
        else:
            print("You have not enough mana")
            raise NotEnoughMana

    def mana_regen(self):
        if self.mp + 20 < self.full_mp:
            self.mp += 20
        else:
            self.mp = self.full_mp


class Enemy(Character):
    def __init__(self, name, hp, atk, dfs):
        super().__init__(name, hp, atk, dfs)