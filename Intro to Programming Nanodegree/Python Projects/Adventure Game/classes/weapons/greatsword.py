# -*- coding: UTF-8
from .weapon import Weapon


class Greatsword(Weapon):
    def __init__(self):
        super().__init__(
            name="Greatsword",
            multiplier=2,
            damage_die=6,
        )
