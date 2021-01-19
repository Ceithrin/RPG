from arts import print_art
from character import NotEnoughMana, PlayerIsDead
from spells import Effect


class Fight:  # pole walki - tutaj dzieje się cała gra
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        
    def get_input(self, message=''):
        return input(message)

    def choose_action(self):
        return self.player.available_spells[int(self.get_input()) - 1]

    def print_help(self):
        for s in range(len(self.player.available_spells)):
            print(f"{s + 1} - {self.player.available_spells[s].return_spell_info()}")

    def fight(self):
        while True:
            self.player.apply_effects()     # TODO added
            print(f"Your hp: {self.player.hp}\nYour mana: {self.player.mp}")
            print(f"{self.enemy.name} hp: {self.enemy.hp}")
            while True:
                try:
                    self.print_help()
                    player_atk = self.player.use_spell(self.choose_action())
                    break
                except NotEnoughMana:
                    pass
                except ValueError:
                    print("\033[0:31mYou have to choose number\033[0m")
                except IndexError:
                    print("\033[0:31mYou have to choose number available on list\033[0m")
            self.player.attack(player_atk, self.enemy)
            if self.enemy.is_dead():
                print(f"\033[32mYou killed {self.enemy.name}\033[0m")
                return
            self.enemy.attack(self.enemy.atk, self.player)
            if self.player.is_dead():
                print_art('death')      # TODO dodany art
                print(f"\033[0:31mYou are dead\033[0m")
                raise PlayerIsDead
            self.player.mana_regen()
