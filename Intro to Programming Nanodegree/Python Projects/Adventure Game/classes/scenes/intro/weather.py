# -*- coding: UTF-8
from classes.interactable import Interactable


class Weather(Interactable):
    def __init__(self):
        super().__init__(
            description="The wind and snow have been particularly brutal "
                        "today. You'd best get inside before you freeze."
        )
