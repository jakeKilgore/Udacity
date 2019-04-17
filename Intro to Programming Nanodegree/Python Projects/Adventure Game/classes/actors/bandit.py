# -*- coding: UTF-8
from .actor import Actor
from ..stats import Stats
from ..weapons.scimitar import Scimitar
from ..weapons.light_crossbow import LightCrossbow
from ..armor.leather_armor import LeatherArmor


class Bandit(Actor):
    def __init__(self):
        super().__init__(
            name="Bandit",
            hit_points=11,
            ability_scores=Stats([11, 12, 12, 10, 10, 10]),
            armor=LeatherArmor(),
            weapons={Scimitar(), LightCrossbow()},
        )
