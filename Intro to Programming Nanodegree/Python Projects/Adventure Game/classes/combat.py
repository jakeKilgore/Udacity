# -*- coding: UTF-8
from .turn_order import TurnOrder
import classes.console as console
import time


class Combat:
    """Class for handling combat between actors.

    Combat is allowed between two groups of actors. When combat is entered, all combatants roll initiative and
    enter a turn order based on that initiative roll. If the attacker combatants surprise the defenders, they will
    each get a turn before continuing normal turn order. Combat continues until all members of the attackers or all
    members of the defenders have left combat.

    Attributes:
        attackers (Party): A collection of combatants initiating combat with the defenders.
        defenders (Party): A collection of combatants being engaged in combat by the attackers.
        surprise (bool): Whether the attackers have surprised the defenders.
        combat_order (TurnOrder): The order in which combatants will take their turn in combat.
    """
    def __init__(self, attackers, defenders, surprise):
        """Constructor for the Combat class.

        Parameters:
            attackers (Party): A collection of actors initiating combat with the defenders.
            defenders (Party): A collection of actors being engaged in combat by the attackers.
            surprise (bool): Whether the attackers have surprised the defenders.
        """
        self.attackers = attackers
        self.defenders = defenders
        self.surprise = surprise
        self.combat_order = TurnOrder(attackers, defenders)

    def engage(self):
        """Begin combat.

        Combat consists of looping through the turn order until either the attackers or defenders have all left combat.
        """
        console.output(f"You are fighting {self.defenders}")
        for character in self.attackers:
            character.enemies = self.defenders
        for character in self.defenders:
            character.enemies = self.attackers

        if self.surprise:
            for placement in self.combat_order:
                if placement.character in self.attackers:
                    placement.character.attack()

        while True:
            for placement in self.combat_order:
                if len(self.attackers) == 0 or len(self.defenders) == 0:
                    return
                if not placement.character.alive:
                    self.combat_order.remove(placement.character)
                    self.attackers.discard(placement.character)
                    self.defenders.discard(placement.character)
                    continue
                placement.character.attack()
                time.sleep(1)
