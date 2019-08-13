from classes.interactable import Interactable


class Confirm(Interactable):
    def __init__(self):
        super().__init__(
            description="Would you like to start over?",
            actions={'yes': lambda: self.restart(True),
                     'no': lambda: self.restart(False)}
        )
        self.play_again = None

    def restart(self, do_again):
        self.play_again = do_again
        return True
