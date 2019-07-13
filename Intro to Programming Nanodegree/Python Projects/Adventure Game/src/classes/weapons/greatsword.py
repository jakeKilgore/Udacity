# -*- coding: UTF-8
from .weapon import Weapon


class Greatsword(Weapon):
    """Class handling the Greatsword weapon type. The greatsword deals 2d6 damage."""
    def __init__(self):
        """Constructor for the Greatsword class."""
        super().__init__(
            name="Greatsword",
            multiplier=2,
            damage_die=6,
        )
