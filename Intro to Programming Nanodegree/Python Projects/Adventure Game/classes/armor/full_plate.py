# -*- coding: UTF-8
from .armor import Armor


class FullPlate(Armor):
    def __init__(self):
        super().__init__(
            armor_class=18,
        )
