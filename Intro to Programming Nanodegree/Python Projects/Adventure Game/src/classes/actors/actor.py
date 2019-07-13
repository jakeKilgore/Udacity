# -*- coding: UTF-8
from ..console import Console
from ..stats import Stats
from ..dice import Dice
from ..armor.armor import Armor
import random


class Actor:
    """Class for handling characters in the story.

    Attributes:
        name (string): Name of the actor.
        max_hit_points (int): The maximum health of the actor.
        hit_points (int): The current health of the actor.
        ability_scores (Stats): Stats assigned to the character to describe their abilities.
        armor (Armor): Armor worn by the actor.
        weapons (Set[Weapon]): Weapons equipped by the character.
        proficiency (int): A general bonus applied to skills the actor is proficient at.
        enemies (Set[Actor]): Valid targets for attack.
        alive (bool): Whether the actor is currently alive.
    """
    def __init__(self, name, hit_points=0, ability_scores=None, armor=None, weapons=None, proficiency=0):
        """Constructor for the Actor class.

        Parameters:
            name (string): Name of the actor. By default, it is the empty string.
            hit_points (int): The maximum health of the actor. By default, it is 0.
            ability_scores (Stats): Stats assigned to the character to describe their abilities.
                                    By default, the default stats are used.
            armor (Armor): Armor worn by the actor. By default, the actor has default armor.
            weapons (Set[Weapon]): Weapons equipped by the character. by default, it is an empty set.
            proficiency (int): A general bonus applied to skills the actor is proficient at.
        """
        self.name = name
        self.max_hit_points = hit_points
        self.hit_points = hit_points
        self.ability_scores = ability_scores if ability_scores is not None else Stats()
        self.armor = armor if armor is not None else Armor()
        self.weapons = weapons if weapons is not None else set()
        self.proficiency = proficiency
        self.enemies = None
        self.alive = True

    def __str__(self):
        """String representation of the Actor class."""
        return self.name

    def initiative(self):
        """Roll initiative to determine combat order.

        Return:
            int: Initiative value for the battle.
        """
        return Dice.roll() + self.ability_scores.dexterity.modifier

    def attack(self):
        """Take a turn in combat and attack an enemy.

        The actor will choose a target and a weapon to attack with. The actor will swing at the target and, if their
        attack roll matches the target's armor, the attack will hit. The damage of the attack is determined by the
        chosen weapon.
        """
        assert (self.enemies is not None and len(self.enemies) > 0), "There are no enemies!"
        target = self.choose_target()
        weapon = self.choose_weapon()
        Console.output(f"{self} attacks {target} with a {weapon}.")
        if self.swing() >= target.block():
            damage = self.damage(weapon)
            target.take_damage(damage)
            Console.output(f"{target} takes {damage} damage. {target} is now at {target.hit_points} health.")
            if target.hit_points <= 0:
                Console.output(f"{target} has died.")
        else:
            Console.output(f"{self} misses.")

    def choose_target(self):
        """Choose a target to attack.

        By default, the actor will choose a random target.
        """
        return random.choice(tuple(self.enemies))

    def choose_weapon(self):
        """Choose a weapon to attack the enemy with.

        By default, the actor will choose a random weapon.
        """
        return random.choice(tuple(self.weapons))

    def swing(self):
        """Roll to hit the target.

        Return:
            int: The attack value to compare against the target's armor class.
        """
        return Dice.roll() + self.proficiency + self.ability_scores.strength.modifier

    def block(self):
        """Attempt to block the target's attack.

        Return:
            int: The actor's armor class.
        """
        return self.armor.armor_class

    def damage(self, weapon):
        """Roll for damage.

        Damage is determined by rolling a number of dice determined by the chosen weapon.

        Parameters:
            weapon (Weapon): The weapon used to damage the target.

        Return:
            int: The amount of damage dealt.
        """
        damage = self.ability_scores.strength.modifier
        for die in range(weapon.multiplier):
            damage += Dice.roll(weapon.damage_die)
        return damage

    def take_damage(self, damage):
        """Reduce the actor's hit points.

        Parameters:
            The damage the actor will take.
        """
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.die()

    def die(self):
        """The actor will die."""
        self.enemies = None
        self.alive = False
