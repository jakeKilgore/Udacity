# -*- coding: UTF-8
from stats import Stats
from combat import Combat
from team import Team
import random

character_stats = {
    'bandit': {
        'stats': Stats([11, 12, 12, 10, 10, 10], 100),
        'weapon': 'scimitar'
    }
}


class Character:
    """Class for handling player and non-player characters."""
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        self.team = Team([self])

    def fight(self, enemy, surprise):
        fight = Combat(self.team, enemy.team, surprise)
        return fight.engage()

    def attack(self, targets):
        target = self.pick_target(targets)
        damage = self.roll_damage()
        target.damage(damage)
        print(f"{self} attacks {target} and deals {damage} damage.")

    def pick_target(self, targets):
        return random.choice(tuple(targets))

    def roll_damage(self):
        damage = 0
        return damage

    def damage(self, damage):
        self.stats.hit_points -= damage
        if self.stats.hit_points <= 0:
            self.die()

    def die(self):
        self.team.remove(self)
