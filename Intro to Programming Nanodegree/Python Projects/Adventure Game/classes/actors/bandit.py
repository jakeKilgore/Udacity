# -*- coding: UTF-8
from .actor import Actor
from ..stats import Stats
from ..weapons.scimitar import Scimitar
from ..weapons.light_crossbow import LightCrossbow
from ..armor.leather_armor import LeatherArmor


class Bandit(Actor):
    """Class for handling the Bandit enemy type.
    The bandit class extends the Actor class.
    """
    def __init__(self, name="Bandit"):
        """Constructor for the Bandit class."""
        super().__init__(
            name=name,
            description="They are wearing patchwork, leather armor, and "
                        "carrying a shortsword and crossbow.",
            hit_points=11,
            ability_scores=Stats(11, 12, 12, 10, 10, 10),
            armor=LeatherArmor(),
            weapons={Scimitar(), LightCrossbow()},
        )
