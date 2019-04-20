import random


class Dice:
    """Class handling dice mechanics."""
    @staticmethod
    def roll(die=20):
        """Roll a dice with a given number of sides.

        Parameters:
            die (int): The number of sides in the die. By default, a twenty-sided die (d20) is used.
        """
        return random.randint(1, die)
