# -*- coding: UTF-8
from classes.actors.player import Player
from classes.interactable import Interactable
from classes.scenes.entrance.entryway import Entryway
from classes.scenes.fight.banditfight import BanditFight
from classes.scenes.intro.introduction import Introduction


def main():
    print()
    game = Interactable(
        description="You're in it! You can exit it, if you want to.",
        actions={'exit': lambda: exit(0)}
    )
    main_character = Player()
    story(main_character, game)
    return


def story(main_character, game):
    game_objects = {'self': main_character, 'game': game}
    Introduction(game_objects).play()
    Entryway(game_objects).play()
    BanditFight(game_objects).play()


if __name__ == "__main__":
    main()
