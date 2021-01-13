from character import *


class Fight:  # pole walki - tutaj dzieje się cała gra
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def choose_action(self, input):
        return {
            '1': 'fireball',
            '2': 'icicle',
            '3': 'default'
        }.get(input, 'default')

    def print_help(self):
        print("\n 1 - Fireball - Damage: 30, Mana Cost: 50"
              "\n 2 - Icicle - Damage: 25, Mana Cost: 40"
              "\n 3 - Normal Attack - Damage: {}, Mana Cost: 0".format(self.player.atk)
              )

    def fight(self):
        while True:
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
                print(f"\033[0:31mYou are dead\033[0m")
                return
            self.player.mana_regen()

print("                  .\n"
      "                   .\n"
      "         /^\     .\n"
      "    /\   \"V\" \n"
      "   /__\   I      O  o\n"
      "  //..\\\  I     .\n"
      "  \].`[/  I\n"
      "  /l\/j\  (]    .  O\n"
      " /. ~~ ,\/I          .\n"
      " \\|L__j^\/I       o\n"
      "  \/--v}  I     o   .\n"
      "  |    |  I   _________\n"
      "  |    |  I c(`       ')o\n"
      "  |    l  I   \.     ,/\n"
      "_/j  L l\_!  _//^---^\\_ \n"
      "Welcome, Young Mage!\n"
      "So you are looking for Adventure and Glory?\n"
      "In front of you is the entrance to The Mage Arena\n"
      "To prove your courage and obtain Power you have to face bloodthirsty monster\n"
      "Shall you enter?\n")

mage = Player(input("What's your name?\n"), 100, 100, 20, 30)

goblin = Enemy("Goblin", 70, 37, 20)
game = Fight(mage, goblin)



print(mage.say_hello())

game.fight()
