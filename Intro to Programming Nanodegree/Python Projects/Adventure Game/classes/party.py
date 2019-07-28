# -*- coding: UTF-8
from collections.abc import Mapping
from .actors.actor import Actor


class Party(Mapping):
    """Class for handling groups of actors working together.

    Attributes:
        members (Dictionary[Actor]): A group of actors working together.
    """
    def __init__(self, members):
        """Constructor for the Party class.

        Parameters:
            members (list[Actor]): A group of actors working together.
        """
        self.members = {}
        for member in members:
            self.members[member.name.lower()] = member

    def __iter__(self):
        """Iterate through the members of the party."""
        for member in self.members.values():
            yield member

    def __getitem__(self, member):
        """Retrieve one of the members of the party, if it is present.

        Parameters:
            member (Actor or str): The member to check for. This may be the name or the Actor object of the member.
        """
        if isinstance(member, Actor):
            key = member.name.lower()
        else:
            key = member
        return self.members.__getitem__(key)

    def __len__(self):
        """The number of members in the party."""
        return self.members.__len__()

    def __str__(self):
        """String representation of the party."""
        string = ""
        for name in self.members:
            string += f"{name} "
        return string

    def discard(self, member):
        """Remove a member from the party, if it is present.

        If the given parameter is not in the party, no error is raised.

        Parameters:
            member (Actor or str): The member to remove. This may be the name or the Actor object of the member.
        """
        if isinstance(member, Actor):
            key = member.name.lower()
        else:
            key = member
        try:
            del self.members[key]
        except KeyError:
            pass
        return None
