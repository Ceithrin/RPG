from arts import print_art
from character import NotEnoughMana
from spells import Effect


class Fight:  # pole walki - tutaj dzieje się cała gra
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def choose_action(self, input):
        return self.player.available_spells[int(input) - 1]
        # return {
        #     '1': 'fireball',
        #     '2': 'icicle',
        #     '3': 'default'
        # }.get(input, 'default')

    def print_help(self):
        for s in range(len(self.player.available_spells)):
            print(f"{s + 1} - {self.player.available_spells[s].return_spell_info()}")
        # print("\n 1 - Fireball - Damage: 30, Mana Cost: 50"
        #       "\n 2 - Icicle - Damage: 25, Mana Cost: 40"
        #       "\n 3 - Normal Attack - Damage: {}, Mana Cost: 0".format(self.player.atk)
        #       )

    def fight(self):
        while True:
            self.player.apply_effects()     # TODO added
            print(f"Your hp: {self.player.hp}\nYour mana: {self.player.mp}")
            print(f"{self.enemy.name} hp: {self.enemy.hp}")
            while True:
                try:
                    self.print_help()
                    player_atk = self.player.use_spell(self.choose_action(input("Choose attack: ")))
                    break
                except NotEnoughMana:
                    pass
            self.player.attack(player_atk, self.enemy)
            if self.enemy.is_dead():
                print(f"\033[32mYou killed {self.enemy.name}\033[0m")
                return
            self.enemy.attack(self.enemy.atk, self.player)
            if self.player.is_dead():
                print_art('death')      # TODO dodany art
                print(f"\033[0:31mYou are dead\033[0m")
                return
            self.player.mana_regen()