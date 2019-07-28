from classes import console
from classes.actors.bandit import Bandit
from classes.combat import Combat
from classes.party import Party
from classes.scenes.scene import Scene


badly_wounded = "You groan and clutch your side. You will need to rest soon and heal your wounds, but for now," \
                "you must press onwards."
wounded = "You aren't badly hurt, and feel confident about moving forwards."
unharmed = "They were no real challenge, and you don't have a single scratch on you. You feel ready to move on."


class BanditFight(Scene):
    def __init__(self, game_objects):
        self.player = game_objects['self']
        super().__init__(
            game_objects,
            setup=[
                "As you enter, though, three people burst into the room from the other end, sprinting towards you.",
                lambda: console.whitespace(2),
                "They are wearing patchwork armor and carrying shortswords and crossbows.",
                "You recognize some of their features as members of the band you are hunting.",
                "They look shocked to see you.",
                lambda: console.whitespace(2),
                "\"Who is that?!\" One of them shouts out in alarm.",
                lambda: console.whitespace(2),
                "\"Who cares?\" Another yells. \"Kill them!\"",
                lambda: console.whitespace(2),
                "Their voices sound panicked, but you have no time to think about why",
                "as they rush towards you with weapons drawn.",
                "You will have to kill them.",
            ],
            resolution=[
                "When the last bandit falls, you wipe the blood off of your blade and sheathe it.",
                lambda: check_health(self.player),
                "Those were only a few members of the larger group, and if you leave now, they might run.",
                "You have to finish this."
            ],
            proceed=False,
        )

    def action(self):
        enemies = Party(
            members=[
                Bandit("bandit1"),
                Bandit("bandit2"),
                Bandit("bandit3"),
            ]
        )
        Combat(Party([self.player]), enemies).engage()


def check_health(player):
    if player.hit_points < player.max_hit_points / 2:
        console.output(badly_wounded, new_line=False)
    elif player.hit_points < player.max_hit_points:
        console.output(wounded, new_line=False)
    elif player.hit_points == player.max_hit_points:
        console.output(unharmed, new_line=False)
