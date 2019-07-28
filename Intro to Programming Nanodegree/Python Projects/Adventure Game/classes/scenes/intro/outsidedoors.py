# -*- coding: UTF-8
from ...interactable import Interactable
import classes.console as console


class OutsideDoors(Interactable):
    """Class for handling the door blocking passage into the tomb in the first scene.

    The door will serve as a tutorial for the command structure for the rest of the game. It has two actions associated
    with it: enter and open. Enter will move the player to the next scene, but it will not work until the player has
    used the Open command.

    Attributes:
        is_open (bool): Whether the doors are open or closed.
    """

    def __init__(self):
        """Constructor for the Door class."""
        super().__init__()
        self.is_open = False
        self.description = "A set of heavy, stone doors."
        self.actions.update({'open': lambda: self.open(), 'enter': lambda: self.enter()})

    def open(self):
        """Open the door, allowing the use of the Enter command."""
        if self.is_open:
            console.output("The doors are already open.")
            return False
        self.is_open = True
        console.output("The heavy doors grind against the ground as you push them open.")
        return False

    def enter(self):
        """Enter the door, triggering the next scene."""
        if not self.is_open:
            console.output("The doors are shut.")
            return False
        return True
