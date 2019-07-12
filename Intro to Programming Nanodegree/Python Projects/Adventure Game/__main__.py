# -*- coding: UTF-8
import classes.actors.bandit as bandit
import classes.actors.player as player
import classes.combat as combat
import classes.party as party


def main():
    main_character = player.Player()
    enemy = random_enemy()
    story(main_character, enemy)
    return


def story(main_character, enemy):
    fight = combat.Combat(party.Party([main_character]), party.Party([enemy]), False)
    fight.engage()


def random_enemy():
    return bandit.Bandit()


if __name__ == "__main__":
    import os
    import sys
    path = os.path.dirname(os.path.join(os.getcwd(), __file__))
    sys.path.append(os.path.normpath(os.path.join(path, '..', '..')))
    main()
