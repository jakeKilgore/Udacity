# -*- coding: UTF-8
from .weapon import Weapon


class Scimitar(Weapon):
    def __init__(self):
        super().__init__(
            multiplier=1,
            damage_die=6,
        )
