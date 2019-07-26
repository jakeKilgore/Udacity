# -*- coding: UTF-8
from .doors import Doors
import classes.scenes.scene as scene
import classes.console as console


class Introduction(scene.Scene):
    """Class for handling the first scene in the game.

    The player will approach a doorway and then enter. This serves as a tutorial for the user input system of the game.

    Attributes:
        doors (Doors): A set of doors blocking the player's way into the tomb.
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
                lambda: console.whitespace(),
                "What would you like to do?",
            ],
            proceed=False,
            objects=objects,
        )
        self.doors = Doors()
        self.objects.update({'doors': self.doors})
