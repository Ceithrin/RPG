from character import *
from main_menu import *
from fight import Fight
from arts import print_art
from spells import Spell, Effect


class Game:

    def __init__(self, m_menu, player=None):
        self.main_menu = m_menu
        self.player = player
        self.intro = "\033[34mWelcome, Young Mage!\n" \
                     "So you are looking for Adventure and Glory?\n" \
                     "In front of you is the entrance to The Mage Arena\n" \
                     "To prove your courage and obtain Power you have to face bloodthirsty monster\033[0m\n\n"
        self.outro = "You have proved your power and defeated everyone... Glory to you!"
        self.enemies = [
            Enemy("Goblin", 70, 37, 20),
            Enemy("Elf", 90, 50, 10)
        ]

    def create_player(self):
        self.player = Player(input("What's your name?\n> "), 100, 100, 20, 30)
        print(self.player.say_hello(), "\n")

    def start_arena(self):
        game1 = Fight(self.player, self.enemies[self.player.lvl-1])
        game1.fight()

    def run(self):
        print_art("mage")
        print(self.intro)
        print("Shall you enter? [y/n]")
        while True:
            i = input("> ")
            try:
                i = i.lower()
                if i in ['y', 'yes']:
                    break
                elif i in ['n', 'no']:
                    self.main_menu.display = True
                    while self.main_menu.display:
                        self.main_menu.display_main_menu()
                        self.main_menu.perform_the_option()
                    print_art("mage")
                    print(self.intro)
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Oops! Seems like that's not the expected answer.")


g = Game(main_menu)
g.run()
g.create_player()

# creating spells
fireball = Spell('Fireball', 30, 50)
icicle = Spell('Icicle', 25, 40)
default = Spell('Default', g.player.atk, 0)
thorns = Spell('Thorns', 40, 60)
speed = Effect('Speed', g.player.atk*2, 0, 5)
# creating effects
rage = Effect('Rage', 10, 0, 3)
# add spells and effects
g.player.available_spells = [fireball, icicle, default]
g.player.effects_on = [rage]

awards = [{"1": ["Attack: +20", 20, g.player.atk],
           "2": ["Defense: +20", 20, g.player.dfs],
           "3": [f"Spell: {thorns.return_spell_info()}", thorns, g.player.available_spells],
           "4": [f"Effect: {speed.return_effect_info()}, Number of rounds: {speed.time - 1}", speed, g.player.effects_on]},
          {"1": ["Attack: +50", 50, g.player.atk],
           "2": ["Defense: +50", 50, g.player.dfs],
           "3": ["Health: +50", 50, g.player.hp]}]

try:
    g.start_arena()
except PlayerIsDead:
    exit()
award = g.player.level_up(awards[g.player.lvl - 1])
try:
    list(awards[g.player.lvl - 2].values())[award][2] += list(awards[g.player.lvl - 2].values())[award][1]
except:     # TODO dodać wyjątek
    list(awards[g.player.lvl - 2].values())[award][2].append(list(awards[g.player.lvl - 2].values())[award][1])
print(f"Option {award + 1} has been added")
try:
    g.start_arena()
except PlayerIsDead:
    exit()
print("\033[34m\n", g.outro)
print_art("victory")
