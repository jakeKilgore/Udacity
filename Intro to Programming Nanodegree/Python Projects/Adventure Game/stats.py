# -*- coding: UTF-8


class Stats:
    def __init__(self, stat_array, hit_points):
        self.strength = stat_array[0]
        self.dexterity = stat_array[1]
        self.constitution = stat_array[2]
        self.intelligence = stat_array[3]
        self.wisdom = stat_array[4]
        self.charisma = stat_array[5]
        self.hit_points = hit_points
