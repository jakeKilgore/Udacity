# -*- coding: UTF-8
import src.classes.actors.bandit as bandit
import src.classes.actors.player as player
import src.classes.combat as combat
import src.classes.party as party
import src.classes.scenes.introduction as introduction


def main():
    print()
    main_character = player.Player()
    enemy = random_enemy()
    story(main_character, enemy)
    return


def story(main_character, enemy):
    #introduction.Introduction().play()
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
