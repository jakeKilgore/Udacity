# -*- coding: UTF-8
from character import Character
from stats import Stats


class Player(Character):
    def __init__(self):
        Character.__init__(self, 'player', Stats([20, 14, 15, 11, 13, 9]), 52)
