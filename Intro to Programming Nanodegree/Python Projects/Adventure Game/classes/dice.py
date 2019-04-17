import random


class Dice:
    @staticmethod
    def roll(die):
        return random.randint(1, die)
