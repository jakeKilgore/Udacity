class Node:

    def __init__(self, priority, symbol=None, left_child=None, right_child=None):
        self.priority = priority
        self.symbol = symbol
        self.left_child = left_child
        self.right_child = right_child

    def __eq__(self, other):
        return (self.priority == other.priority) and (self.symbol == other.symbol)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if self.priority == other.priority:
            if self.symbol is None:
                return True
            if other.symbol is None:
                return False
            return self.symbol < other.symbol
        else:
            return self.priority < other.priority

    def __le__(self, other):
        return (self < other) or (self == other)

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)

    def __repr__(self):
        if self.symbol is None:
            return f"({self.priority})"
        return f"({self.symbol}: {self.priority})"
