# -*- coding: UTF-8
from ...interactable import Interactable
import classes.console as console


class InsideDoors(Interactable):

    def __init__(self):
        """Constructor for the Door class."""
        super().__init__(
            description="The heavy, stone doors you just entered through. "
                        "The wind closed them.",
            actions={'open': lambda: self.open(),
                     'enter': lambda: self.enter()},
        )

    def open(self):
        """The doors will refuse to open."""
        console.output("The doors seem to be sealed shut. "
                       "Hopefully you'll be able to open them when you leave.")
        return False

    def enter(self):
        """The door is sealed shut and will not open."""
        console.output("The doors are shut.")
        return False
