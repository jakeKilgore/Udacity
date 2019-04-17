# -*- coding: UTF-8
from .weapon import Weapon


class LightCrossbow(Weapon):
    def __init__(self):
        super().__init__(
            name="Light Crossbow",
            multiplier=1,
            damage_die=8,
        )
