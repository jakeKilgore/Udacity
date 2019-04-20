# -*- coding: UTF-8
from .turn_order import TurnOrder
import time
# TODO: Add documentation


class Combat:
    def __init__(self, attackers, defenders, surprise):
        self.attackers = attackers
        self.defenders = defenders
        self.surprise = surprise
        self.combat_order = TurnOrder(attackers.union(defenders))

    def engage(self):
        print(f"You are fighting {self.defenders}")
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
