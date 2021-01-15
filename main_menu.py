class MainMenu:

    def __init__(self):
        self.options = {"1": ["Join the adventure", self.launch_the_game],
                        "2": ["Read the instructions", self.display_instructions],
                        "3": ["Escape", exit]}
        self.display = False

    def display_options(self):
        for i in range(len(list(self.options.keys()))):
            print(f"{i + 1} - {list(self.options.values())[i][0]}")

    def display_main_menu(self):
        print("\nWelcome to the Mage Arena!\n"
              "Below, there are some options, you might want to try.\n")
        self.display_options()

    def choose_option(self):
        while True:
            i = input("> ")
            if i in list(self.options.keys()):
                return int(i) - 1
            print("That was sneaky, but we thought about it in advance.\nTry choosing something from the list.")

    def perform_the_option(self):
        opt = list(self.options.values())[self.choose_option()][1]
        opt()

    def launch_the_game(self):
        self.display = False

    @staticmethod
    def display_instructions():
        print("\nYour task is to kill two terrifying monsters.\n"
              "You both attack in turns, after every turn your mana regenerates by 20 points.\n"
              "Good luck!")   # TODO

        input("\nPress enter to continue.")


main_menu = MainMenu()