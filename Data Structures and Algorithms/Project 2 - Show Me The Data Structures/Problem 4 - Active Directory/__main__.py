class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = set()
        self.users = set()

    def __repr__(self):
        return self.name

    def add_group(self, group):
        self.groups.add(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    visited = set()
    return recursive_group_search(user, group, visited)

def recursive_group_search(user, group, visited):
    if group in visited:
        return False
    visited.add(group)
    if user in group.users:
        return True
    for sub_group in group.groups:
        if recursive_group_search(user, sub_group, visited):
            return True
    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

assert is_user_in_group(sub_child_user, sub_child), "Cannot find user in group."
assert is_user_in_group(sub_child_user, child), "Cannot find user in child group."
assert is_user_in_group(sub_child_user, parent), "Cannot find user in grandchild group."
assert not is_user_in_group("fake_user", parent), "Found non-existant user."
