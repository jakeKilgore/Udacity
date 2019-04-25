# -*- coding: UTF-8
from collections.abc import Mapping
from ..classes.actors.actor import Actor


class Party(Mapping):
    def __init__(self, members):
        self.members = {}
        for member in members:
            self.members[member.name] = member

    def __iter__(self):
        for member in self.members.values():
            yield member

    def __getitem__(self, member):
        if isinstance(member, Actor):
            key = member.name
        else:
            key = member
        return self.members.__getitem__(key)

    def __len__(self):
        return self.members.__len__()

    def __str__(self):
        string = ""
        for name in self.members:
            string += f"{name} "
        return string

    def discard(self, member):
        if isinstance(member, Actor):
            key = member.name
        else:
            key = member
        try:
            del self.members[key]
        except KeyError:
            pass
        return None
