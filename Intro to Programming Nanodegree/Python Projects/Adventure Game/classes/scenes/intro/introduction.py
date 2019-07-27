# -*- coding: UTF-8
from .outsidedoors import OutsideDoors
import classes.scenes.scene as scene
import classes.console as console


class Introduction(scene.Scene):
    """Class for handling the first scene in the game.

    The player will approach a doorway and then enter. This serves as a tutorial for the user input system of the game.
    """

    def __init__(self, objects):
        """Constructor for the Introduction scene.

        Parameters:
            objects (dict[str,Interactable]): A collection of interactable objects to add to the scene.
        """
        super().__init__(
            setup=[
                "The wind buffets against you as you trudge through the snow.",
                lambda: scene.pause(),
                "For the past several months, a band of brigands has been harassing traders on the road out of Liska,",
                "and the local lord is offering a large bounty to anyone who can bring them to justice.",
                lambda: scene.pause(),
                "You were able to track down someone who used to work with them, "
                "and they told you that the group runs out of a long-abandoned tomb set into a nearby cliff face.",
                lambda: scene.pause(),
                lambda: console.whitespace(2),
                "You take cover from the harsh weather in the stone entryway of the barrow and check your equipment.",
                lambda: scene.pause(),
                "You are wearing a set of steel plate armor, and carry a hefty greatsword in a scabbard on your back.",
                lambda: scene.pause(),
                "The heavy, stone doors of the tomb loom in front of you.",
                lambda: scene.pause(),
                lambda: console.whitespace(2),
                "What would you like to do?",
            ],
            resolution=[
                "Just as soon as you pass through the doorway, a gust of wind blows out from the depths of the tomb.",
                lambda: scene.pause(),
                "You stumble a bit as you brace against the gale, and the doors slam shut behind you.",
                lambda: scene.pause(),
                "As the doors seal, the wind stops, and the dust of the tomb slowly settles.",
            ],
            proceed=False,
            objects=objects,
        )
        doors = OutsideDoors()
        self.objects.update({'doors': doors})

