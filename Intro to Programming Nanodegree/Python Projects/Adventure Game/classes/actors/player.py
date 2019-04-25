# -*- coding: UTF-8
from .actor import Actor
from ..stats import Stats
from ..armor.full_plate import FullPlate
from ..weapons.greatsword import Greatsword


class Player(Actor):
    """Class handling the Player's character. The Player class extends the Actor class."""
    def __init__(self):
        """Constructor for the Player class."""
        super().__init__(
            name="Player",
            hit_points=58,
            ability_scores=Stats(18, 14, 16, 11, 13, 9),
            armor=FullPlate(),
            weapons={Greatsword()},
            proficiency=3,
        )

    def choose_target(self):
        """Choose a target to attack.

        This overrides the Actor class' choose_target method. The player will choose a target from the list of enemies.
        """
        print("Choose a target:")
        print(self.enemies)
        while True:
            target = input()
            if target in self.enemies:
                return self.enemies[target]
