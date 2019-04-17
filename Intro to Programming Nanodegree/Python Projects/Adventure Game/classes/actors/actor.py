# -*- coding: UTF-8
from ..stats import Stats
from ..dice import Dice
import random


class Actor:
    """Class for handling characters in the story.

    Attributes:
        hit_points (int): Health of the actor.
        ability_scores (Stats): Stats assigned to the character to describe their abilities.
        armor (Armor): Armor worn by the actor.
        weapons (Set[Weapon]): Weapons equipped by the character.
        proficiency (int): A general bonus applied to skills the actor is proficient at.
    """
    def __init__(self, name="", hit_points=0, ability_scores=None, armor=None, weapons=None, proficiency=0):
        self.name = name
        self.max_hit_points = hit_points
        self.hit_points = hit_points
        self.ability_scores = ability_scores
        self.armor = armor
        self.weapons = weapons
        self.proficiency = proficiency
        self.enemies = None
        self.alive = True

    def __str__(self):
        return self.name

    def initiative(self):
        return Dice.roll(20) + Stats.modifier(self.ability_scores.dexterity)

    def attack(self):
        assert (self.enemies is not None and len(self.enemies) > 0), "There are no enemies!"
        target = self.choose_target()
        print(f"{self} attacks {target}.")
        if self.swing() >= target.block():
            damage = self.damage()
            target.take_damage(damage)
            print(f"{target} takes {damage} damage.")
        else:
            print(f"{self} misses.")

    def choose_target(self):
        return random.choice(tuple(self.enemies))

    def choose_weapon(self):
        return random.choice(tuple(self.weapons))

    def swing(self):
        return Dice.roll(20) + self.proficiency + Stats.modifier(self.ability_scores.strength)

    def block(self):
        return self.armor.armor_class

    def damage(self):
        weapon = self.choose_weapon()
        damage = Stats.modifier(self.ability_scores.strength)
        for die in range(weapon.multiplier):
            damage += Dice.roll(weapon.damage_die)
        return damage

    def take_damage(self, damage):
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.die()

    def die(self):
        self.alive = False
