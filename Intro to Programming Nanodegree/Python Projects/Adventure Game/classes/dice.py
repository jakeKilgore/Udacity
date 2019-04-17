import random


class Dice:
    @staticmethod
    def roll(die=20):
        return random.randint(1, die)
