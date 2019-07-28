# -*- coding: UTF-8
from classes import console
from classes.interactable import Interactable


class Coffins(Interactable):
    def __init__(self, player):
        super().__init__(
            description="Old, wooden coffins. They look old, but they're in good shape.",
            actions={'loot': lambda: self.loot()},
        )
        self.confirm = False
        self.player = player

    def loot(self):
        if self.confirm:
            console.output("You find a few old, copper coins among the well-preserved bodies. You monster.")
            self.player.proficiency -= 1
        else:
            console.output("Are you sure? Stealing from the dead is said to bring bad luck.")
            self.confirm = True
        return False
