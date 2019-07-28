# -*- coding: UTF-8
from classes.scenes.intro.weather import Weather
from .outsidedoors import OutsideDoors
# -*- coding: UTF-8
import classes.scenes.scene as scene
import classes.console as console


class Introduction(scene.Scene):
    """Class for handling the first scene in the game.

    The player will approach a doorway and then enter. This serves as a tutorial for the user input system of the game.
    """

    def __init__(self, game_objects):
        """Constructor for the Introduction scene."""
        super().__init__(
            game_objects,
            setup=[
                "The wind buffets against you as you trudge through the snow.",
                "For the past several months, a band of brigands has been harassing traders on the road out of Liska,",
                "and the local lord is offering a large bounty to anyone who can bring them to justice.",
                lambda: console.whitespace(2),

                "You were able to track down someone who used to work with them, "
                "and they told you that the group runs out of a long-abandoned tomb set into a nearby cliff face.",
                "You take cover from the harsh weather in the stone entryway of the barrow and check your equipment.",
                "You are wearing a set of steel plate armor, and carry a hefty greatsword in a scabbard on your back.",
                "The heavy, stone doors of the tomb loom in front of you.",

                lambda: console.whitespace(2),
                "What would you like to do?",
            ],
            resolution=[
                "Just as soon as you pass through the doorway, a gust of wind blows out from the depths of the tomb.",
                "You stumble a bit as you brace against the gale, and the doors slam shut behind you.",
                "As the doors seal, the wind stops, and the dust of the tomb slowly settles.",
            ],
            proceed=False,
        )
        doors = OutsideDoors()
        weather = Weather()
        self.objects.update({'doors': doors, 'weather': weather})

