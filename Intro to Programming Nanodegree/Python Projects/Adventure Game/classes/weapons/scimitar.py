# -*- coding: UTF-8
from .weapon import Weapon


class Scimitar(Weapon):
    """Class handling the Scimitar weapon type.
    The Scimitar deals 1d6 damage.
    """
    def __init__(self):
        """Constructor for the Scimitar class."""
        super().__init__(
            name="Scimitar",
            multiplier=1,
            damage_die=6,
        )
