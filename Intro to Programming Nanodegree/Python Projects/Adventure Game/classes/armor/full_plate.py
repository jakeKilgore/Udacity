# -*- coding: UTF-8
from .armor import Armor


class FullPlate(Armor):
    """Class for handling the Full Plate armor type. Full Plate has an armor class of 18."""
    def __init__(self):
        """Constructor for the FullPlate class."""
        super().__init__(
            armor_class=18,
        )
