from character import *
from main_menu import *
from fight import Fight
from arts import print_art
from spells import Spell, Effect


class Game:

    def __init__(self, m_menu):
        self.main_menu = m_menu
        self.intro = "Welcome, Young Mage!\n" \
                     "So you are looking for Adventure and Glory?\n" \
                     "In front of you is the entrance to The Mage Arena\n" \
                     "To prove your courage and obtain Power you have to face bloodthirsty monster\n\n"

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

mage = Player(input("What's your name?\n> "), 100, 100, 20, 30)
# creating spells
fireball = Spell('Fireball', 30, 50)
icicle = Spell('Icicle', 25, 40)
default = Spell('Default', mage.atk, 0)
# creating effects
rage = Effect('Rage', 10, 0, 3)
# add spells and effects
mage.available_spells = [fireball, icicle, default]
mage.effects_on = [rage]

goblin = Enemy("Goblin", 70, 37, 20)
game = Fight(mage, goblin)

print(mage.say_hello(), "\n")

game.fight()

