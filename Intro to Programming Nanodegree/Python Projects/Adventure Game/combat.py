# -*- coding: UTF-8
import queue


class Combat:
    def __init__(self, attackers, defenders, surprise):
        self.attackers = attackers
        self.defenders = defenders
        self.surprise = surprise
        self.combat_order = queue.Queue()

    def engage(self):
        print(f"You are fighting {self.defenders}")
        if self.surprise:
            for attacker in self.attackers:
                attacker.attack(self.defenders)

        for attacker in self.attackers:
            attacker.attack(self.defenders)
        for defender in self.defenders:
            defender.attack(self.attackers)
