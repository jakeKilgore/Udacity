# -*- coding: UTF-8
from .weapon import Weapon


class LightCrossbow(Weapon):
    def __init__(self):
        super().__init__(
            multiplier=1,
            damage_die=8,
        )
