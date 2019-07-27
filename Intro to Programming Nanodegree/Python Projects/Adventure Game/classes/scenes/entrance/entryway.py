import classes.console as console
import classes.scenes.scene as scene
from classes.scenes.entrance.braziers import Braziers
from classes.scenes.entrance.coffins import Coffins
from classes.scenes.entrance.insidedoors import InsideDoors


class Entryway(scene.Scene):
    def __init__(self, objects):
        super().__init__(
            setup=[
                "You stand in the middle of a large, stone room.",
                scene.pause(),
                "Thick pillars hold up the ceiling and the walls are lined with alcoves, each holding a coffin.",
                scene.pause(),
                "A pair of braziers flank an open doorway leading deeper into the tomb.",
                scene.pause(),
                console.whitespace(),
                "Down the next corridor, you can hear some sort of commotion.",
            ],
            proceed=False,
            objects=objects,
        )
        doors = InsideDoors()
        coffins = Coffins(self.objects['self'])
        braziers = Braziers()
        corridor
        self.objects.update({'doors': doors, 'coffins': coffins, 'braziers': braziers})

