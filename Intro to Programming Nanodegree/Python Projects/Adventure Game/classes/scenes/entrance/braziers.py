from classes.interactable import Interactable


class Braziers(Interactable):
    def __init__(self):
        super().__init__()
        self.description = "A pair of squat braziers, filled with coal. The fires are burning low."
