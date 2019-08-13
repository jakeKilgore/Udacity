# -*- coding: UTF-8


class Weapon:
    """Class representing the weapons wielded by actors.

    When an actor wants to attack another actor, they roll a 20-sided die
    and add their proficiency bonus as well as their strength or dexterity
    modifier based on the type of weapon. If an attack beats the opponent's
    armor class, the actor rolls the damage die of the weapon a number of
    times equal to the weapon's multiplier and then add their strength or
    dexterity modifier based on the type of weapon.

    Attributes:
        name (string): The name of the weapon.
        multiplier (int): The number of times the damage die is rolled after
            a successful attack.
        damage_die (int): The number of sides on the die used to determine
            weapon damage.
    """
    def __init__(self, name, multiplier=0, damage_die=0):
        """Constructor for the Weapon class.

        Parameters:
            name (string): The name of the weapon.
            multiplier (int): The number of times the damage die is rolled
                after a successful attack.
            damage_die (int): The number of sides on the die used to determine
                weapon damage.
        """
        self.name = name
        self.multiplier = multiplier
        self.damage_die = damage_die

    def __str__(self):
        """String representation of the Weapon class."""
        return self.name
