# -*- coding: UTF-8
from .armor import Armor

class LeatherArmor(Armor):
    def __init__(self):
        super().__init__(
            armor_class=11,
        )
