# -*- coding: UTF-8
from classes.interactable import Interactable


class Corridor(Interactable):
    def __init__(self):
        super().__init__(
            description="There is an open doorway leading to a dark corridor. "
                        "It turns, so you can't see to the next room.",
            actions={'enter': lambda: self.enter()},
        )

    def enter(self):
        return True
