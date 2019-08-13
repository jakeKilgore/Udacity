# -*- coding: UTF-8
import classes.console as console
import classes.scenes.scene as scene
from classes.scenes.entrance.braziers import Braziers
from classes.scenes.entrance.coffins import Coffins
from classes.scenes.entrance.corridor import Corridor
from classes.scenes.entrance.insidedoors import InsideDoors


class Entryway(scene.Scene):
    def __init__(self, game_objects):
        player = game_objects['self']
        doors = InsideDoors()
        coffins = Coffins(player)
        braziers = Braziers()
        corridor = Corridor()
        super().__init__(
            game_objects,
            setup=[
                "You stand in the middle of a large, stone room.",

                "Thick pillars hold up the ceiling, and the walls are lined "
                "with alcoves, each holding a coffin.",

                "A pair of braziers flank an open doorway leading deeper "
                "into the tomb.",

                "Down the next corridor, you can hear some sort of commotion.",
                lambda: console.whitespace(2),

                "What would you like to do?",
            ],
            resolution=[
                "As you walk down the corridor, it gets darker and darker",
                "until you have to run your hand against the wall to navigate "
                "the winding tunnel.",

                "Occasionally, you feel the empty space of a doorway, but the "
                "rooms along the side are pitch-black "
                "and you can hear yelling ahead of you.",

                "Eventually, you see a light, and emerge into another room.",
            ],
            proceed=False,
            objects={'doors': doors, 'coffins': coffins, 'braziers': braziers,
                     'corridor': corridor}
        )
