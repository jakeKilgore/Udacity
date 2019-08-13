from classes import console
from classes.scenes.game_over.confirm import Confirm
from classes.scenes.scene import Scene


death = "You fall to the ground, slain. " \
        "Hopefully the next adventurer has better luck than you did."
victory = "You have reached the end of the game so far."


class End(Scene):
    def __init__(self, game_objects):
        self.confirm = Confirm()
        player = game_objects['self']
        super().__init__(
            game_objects,
            setup=[
                lambda: player_status(player),
                lambda: console.whitespace(),
                "Would you like to play again?",
            ],
            proceed=False,
            objects={'confirm': self.confirm}
        )

    def action(self, noun=None, verb=None):
        return super().action(noun='confirm')


def player_status(player):
    if player.alive:
        console.output(victory)
    else:
        console.output(death)
