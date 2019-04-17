# -*- coding: UTF-8
from .actor import Actor
from ..stats import Stats
from ..armor.full_plate import FullPlate
from ..weapons.greatsword import Greatsword


class Player(Actor):
    def __init__(self):
        super().__init__(
            name="Player",
            hit_points=58,
            ability_scores=Stats([18, 14, 16, 11, 13, 9]),
            armor=FullPlate(),
            weapons={Greatsword()},
            proficiency=3,
        )
