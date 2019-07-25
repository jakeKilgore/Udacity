from collections import Set

from .console import Console


class Interactable:
    def __init__(self):
        self.description = None
        self.actions = {'Look': lambda: self.look()}

    def look(self):
        assert (self.description is not None), "This object has no description."
        Console.output(self.description)
        return False
