# -*- coding: UTF-8
from .weapon import Weapon


class Scimitar(Weapon):
    def __init__(self):
        super().__init__(
            name="Scimitar",
            multiplier=1,
            damage_die=6,
        )
