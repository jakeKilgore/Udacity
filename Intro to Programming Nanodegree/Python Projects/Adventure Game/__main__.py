# -*- coding: UTF-8
from character import Character, character_stats
from player import Player


def main():
    main_character = Player()
    enemy = random_enemy()
    story(main_character, enemy)
    return


def story(main_character, enemy):
    main_character.fight(enemy, False)


def random_enemy():
    return Character('bandit', character_stats['bandit'])


if __name__ == "__main__":
    main()
