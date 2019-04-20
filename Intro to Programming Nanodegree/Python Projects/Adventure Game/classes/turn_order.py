# -*- coding: UTF-8
# TODO: Add documentation


class TurnOrder:
    def __init__(self, members):
        self.head = None
        for member in members:
            self.add(member)

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __str__(self):
        string = ""
        for placement in self:
            string += f"{placement.character}: {placement.initiative}"
            if placement.next is not None:
                string += "\n"
        return string

    def add(self, member):
        member_node = Placement(member)
        if self.head is None or member_node > self.head:
            member_node.next = self.head
            self.head = member_node
            return
        for placement in self:
            if placement.next is None:
                placement.next = member_node
                return
            if placement.next < member_node:
                member_node.next = placement.next
                placement.next = member_node
                return

    def remove(self, member):
        if self.head.character is member:
            self.head = self.head.next
            return
        for placement in self:
            if placement.next is None:
                raise ValueError(f"{member} is not in the turn order.")
            if placement.next.character is member:
                placement.next = placement.next.next
                return


class Placement:
    def __init__(self, character):
        self.character = character
        self.initiative = character.initiative()
        self.next = None

    def __eq__(self, other):
        return self.initiative == other.initiative

    def __ne__(self, other):
        return self.initiative != other.initiative

    def __lt__(self, other):
        return self.initiative < other.initiative

    def __le__(self, other):
        return self.initiative <= other.initiative

    def __gt__(self, other):
        return self.initiative > other.initiative

    def __ge__(self, other):
        return self.initiative < other.initiative
