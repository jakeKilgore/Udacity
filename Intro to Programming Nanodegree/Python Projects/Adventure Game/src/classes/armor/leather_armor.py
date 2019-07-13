# -*- coding: UTF-8
from .armor import Armor


class LeatherArmor(Armor):
    """Class for handling the Full Plate armor type. Full Plate has an armor class of 11."""
    def __init__(self):
        """Constructor for the LeatherArmor class."""
        super().__init__(
            armor_class=11,
        )
