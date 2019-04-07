# -*- coding: UTF-8


class Team:
    def __init__(self, members):
        self.members = set(members)

    def __iter__(self):
        return self.members.__iter__()

    def __len__(self):
        return self.members.__len__()

    def remove(self, member):
        self.members.remove(member)
