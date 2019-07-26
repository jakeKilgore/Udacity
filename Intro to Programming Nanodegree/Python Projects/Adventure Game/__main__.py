# -*- coding: UTF-8
import classes.actors.bandit as bandit
import classes.actors.player as player
import classes.scenes.introduction.introduction as introduction
import classes.interactable as interactable


def main():
    print()
    game = interactable.Interactable()
    game.actions.update({'exit': lambda: exit(0)})
    game.description = "You're in it! You can exit it, if you want to."
    main_character = player.Player()
    story(main_character, game)
    return


def story(main_character, game):
    introduction.Introduction({'self': main_character, 'game': game}).play()


def random_enemy():
    return bandit.Bandit()


if __name__ == "__main__":
    import os
    import sys
    path = os.path.dirname(os.path.join(os.getcwd(), __file__))
    sys.path.append(os.path.normpath(os.path.join(path, '..', '..')))
    main()
