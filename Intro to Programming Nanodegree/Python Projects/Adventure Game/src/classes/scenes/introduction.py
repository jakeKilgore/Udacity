# -*- coding: UTF-8
from .scene import Scene
from ..console import Console
import time


class Introduction(Scene):
    def __init__(self):
        super().__init__(
            setup=[
                "The wind buffets against you as you trudge through the snow.",
                lambda: time.sleep(.5),
                "For the past several months, a band of brigands has been harassing traders on the road out of Liska,",
                "and the local lord is offering a large bounty to anyone who can bring them to justice.",
                lambda: time.sleep(.5),
                "You were able to track down someone who used to work with them,"
                "and they told you that the group runs out of a long-abandoned tomb set into a nearby cliff face.",
                lambda: time.sleep(.5),
                lambda: Console.whitespace(2),
                "You take cover from the harsh weather in the stone entryway of the barrow and check your equipment.",
                lambda: time.sleep(.5),
                "You are wearing a set of steel plate armor, and carry a hefty greatsword in a scabbard on your back.",
                lambda: time.sleep(.5),
                "The heavy, stone doors of the tomb loom in front of you.",
                lambda: time.sleep(.5),
                lambda: Console.whitespace(),
                "What would you like to do?",
            ]
        )

    def action(self):
        input = Console.user_action()
