from random import randint


class Die:
    # kostka do gry, będzie służyła do losowania statystyk
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)