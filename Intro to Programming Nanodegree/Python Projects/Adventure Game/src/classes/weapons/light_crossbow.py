# -*- coding: UTF-8
from .weapon import Weapon


class LightCrossbow(Weapon):
    """Class handling the Light Crossbow weapon type. The Light Crossbow deals 1d8 damage."""
    def __init__(self):
        """Constructor for the LightCrossbow class."""
        super().__init__(
            name="Light Crossbow",
            multiplier=1,
            damage_die=8,
        )
