# -*- coding: UTF-8
import classes.console as console


class Interactable:
    """Class handling objects in each scene.

    Attributes:
        description (str): A text description of the object.
        actions (dict[str,lambda]): A dictionary of action names to their
            associated functions.
    """
    def __init__(self, description, actions=None):
        """Constructor for the Interactable class."""
        self.description = description
        self.actions = {'look': lambda: self.look()}
        if type(actions) is dict:
            self.actions.update(actions)

    def look(self):
        """Display the object's description."""
        assert (self.description is not None), f"{self} has no description."
        console.output(self.description)
        return False
