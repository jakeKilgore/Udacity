# -*- coding: UTF-8


class Weapon:
    def __init__(self, name, multiplier=0, damage_die=0):
        self.name = name
        self.multiplier = multiplier
        self.damage_die = damage_die

    def __str__(self):
        return self.name