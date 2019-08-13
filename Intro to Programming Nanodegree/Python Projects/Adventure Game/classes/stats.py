# -*- coding: UTF-8


class Stats:
    """Class handling the ability scores of actors. Ability scores govern how
    good the actor is at related skills.

    Ability scores range between 1 and 30 and give a bonus modifier equal to
    (score - 10) / 2 to associated skills. By default, all stats are 10.

    Attributes:
        strength (int): Measures the actor's bodily power and
            athletic training.
        dexterity (int): Measures the actor's agility, reflexes, and balance.
        constitution (int): Measures the actor's health, stamina,
            and vital force.
        intelligence (int): Measures the actor's mental acuity,
            accuracy of recall, and ability to reason.
        wisdom (int): Measures the actor's attunement to the world around
            them, perceptiveness, and intuition.
        charisma (int): Measures the actor's ability to interact effectively
            with others.
    """
    def __init__(self, strength=10, dexterity=10, constitution=10,
                 intelligence=10, wisdom=10, charisma=10):
        """Constructor for the Stats class.

        Parameters:
            strength (int): The actor's strength ability score.
            dexterity (int): The actor's dexterity ability score.
            constitution (int): The actor's constitution ability score.
            intelligence (int): The actor's intelligence ability score.
            wisdom (int): The actor's wisdom ability score.
            charisma (int): The actor's charisma ability score.
        """
        self.strength = Stat(strength)
        self.dexterity = Stat(dexterity)
        self.constitution = Stat(constitution)
        self.intelligence = Stat(intelligence)
        self.wisdom = Stat(wisdom)
        self.charisma = Stat(charisma)


class Stat:
    """Class handling the individual ability scores of the actor.

    Attributes:
        value (int): The value tied to the ability score.
        modifier (int): The bonus applied to skills tied to the ability score.
    """
    def __init__(self, value):
        """Constructor for the Stat class.

        Parameters:
            value (int): The value tied to the ability score.
        """
        self.value = value
        self.modifier = int((value - 10) / 2)
