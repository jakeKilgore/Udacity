from collections import Set

import classes.console as console


class Interactable:
    """Class handling objects in each scene.

    Attributes:
        description (str): A text description of the object.
        actions (dict[str,lambda]): A dictionary of action names to their associated functions.
    """
    def __init__(self):
        """Constructor for the Interactable class."""
        self.description = None
        self.actions = {'look': lambda: self.look()}

    def look(self):
        """Display the object's description."""
        assert (self.description is not None), "This object has no description."
        console.output(self.description)
        return False
