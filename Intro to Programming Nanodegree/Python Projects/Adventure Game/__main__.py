# -*- coding: UTF-8
from classes.actors.bandit import Bandit
from classes.actors.player import Player
from classes.combat import Combat
from classes.party import Party


def main():
    main_character = Player()
    enemy = random_enemy()
    story(main_character, enemy)
    return


def story(main_character, enemy):
    combat = Combat(Party([main_character]), Party([enemy]), False)
    print(combat.combat_order)
    combat.engage()


def random_enemy():
    return Bandit()


if __name__ == "__main__":
    main()
