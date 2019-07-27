from classes import console
from classes.interactable import Interactable


class Coffins(Interactable):
    def __init__(self, player):
        super().__init__()
        self.description = "Old, wooden coffins. They seem well-preserved inside the tomb."
        self.confirm = False
        self.player = player
        self.actions.update({'loot': lambda: self.loot()})

    def loot(self):
        if self.confirm:
            console.output("You find a few old, copper coins among the bodies. You monster.")
            self.player.proficiency -= 1
        else:
            console.output("Are you sure? Stealing from the dead is said to bring bad luck.")
            self.confirm = True
        return False
