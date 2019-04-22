# -*- coding: UTF-8


class TurnOrder:
    """Class for handling the order of turns in combat.

    TurnOrder is implemented as an ordered, singly-linked list made up of Placement objects. They are ordered from
    highest-initiative combatant to lowest-initiative combatant.

    Attributes:
        head (Placement): The first placement in the combat order.
    """
    def __init__(self, combatants):
        """Constructor for the TurnOrder class.

        Parameters:
            combatants (Set[Actor]): A collection of actors taking part in the combat.
        """
        self.head = None
        for member in combatants:
            self.add(member)

    def __iter__(self):
        """An iterator allowing traversal of the TurnOrder list."""
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __str__(self):
        """String representation of the current turn order."""
        string = ""
        for placement in self:
            string += f"{placement.character}: {placement.initiative}"
            if placement.next is not None:
                string += "\n"
        return string

    def add(self, combatant):
        """Add a combatant to the turn order.

        Parameters:
            combatant (Actor): The combatant to add to the turn order.
        """
        combatant_node = Placement(combatant)
        if self.head is None or combatant_node > self.head:
            combatant_node.next = self.head
            self.head = combatant_node
            return
        for placement in self:
            if placement.next is None:
                placement.next = combatant_node
                return
            if placement.next < combatant_node:
                combatant_node.next = placement.next
                placement.next = combatant_node
                return

    def remove(self, combatant):
        """Remove a combatant from the turn order.

        Parameters:
            combatant (Actor): The combatant to be removed from the turn order.
        """
        if self.head.character is combatant:
            self.head = self.head.next
            return
        for placement in self:
            if placement.next is None:
                raise ValueError(f"{combatant} is not in the turn order.")
            if placement.next.character is combatant:
                placement.next = placement.next.next
                return


class Placement:
    """Class handling the nodes in the TurnOrder linked list.

    Attributes:
        character (Actor): The character who will act on this turn.
        initiative (int): The value determining a character's place in the turn order. Higher initiatives go first.
        next (Placement): The next placement in the turn order.
    """
    def __init__(self, character):
        """Constructor for the Placement class.

        Parameters:
            character (Actor): The character who will act on this turn.
        """
        self.character = character
        self.initiative = character.initiative()
        self.next = None

    def __eq__(self, other):
        """Return whether this Placement is equal to another Placement."""
        return self.initiative == other.initiative

    def __ne__(self, other):
        """Return whether this Placement is not equal to another Placement."""
        return self.initiative != other.initiative

    def __lt__(self, other):
        """Return whether this Placement is less than another Placement."""
        return self.initiative < other.initiative

    def __le__(self, other):
        """Return whether this Placement is less than or equal to another Placement."""
        return self.initiative <= other.initiative

    def __gt__(self, other):
        """Return whether this Placement is greater than another Placement."""
        return self.initiative > other.initiative

    def __ge__(self, other):
        """Return whether this Placement is greater than or equal to another Placement."""
        return self.initiative < other.initiative
