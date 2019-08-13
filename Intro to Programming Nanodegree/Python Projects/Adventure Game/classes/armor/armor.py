# -*- coding: UTF-8


class Armor:
    """Class handling armor worn by actors.

    Armor has a value called armor class. An attacker must beat the armor
    class of the defender on an attack roll in order to deal damage.

    Attributes:
        armor_class (int): A value describing how well the armor protects
            the wearer.
    """
    def __init__(self, armor_class=10):
        """Constructor for the Armor class.

        Parameters: armor_class (int): A value describing how well the armor
        protects the wearer. By default, an unarmored actor has an armor
        class of 10.
        """
        self.armor_class = armor_class
