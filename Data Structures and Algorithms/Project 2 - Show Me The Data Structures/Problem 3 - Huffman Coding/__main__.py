import sys
from priority_queue import Priority_Queue

def main():
    codes = {}

    a_great_sentence = "The bird is the word"

    print(f"The size of the data is: {sys.getsizeof(a_great_sentence)}")
    print(f"The content of the data is: {a_great_sentence}")

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print(f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
    print(f"The content of the encoded data is: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)

    print(f"The size of the decoded data is: {sys.getsizeof(decoded_data)}")
    print(f"The content of the encoded data is: {decoded_data}")

def huffman_encoding(data):
    return None, None

def huffman_decoding(data, tree):
    return None, None

def test_priority_queue():
    priority_queue = Priority_Queue()
    priority_queue.insert(10)
    assert priority_queue.heap == [10]
    priority_queue.insert(4)
    assert priority_queue.heap == [4, 10]
    priority_queue.insert(15)
    assert priority_queue.heap == [4, 10, 15]
    priority_queue.pull()
    assert priority_queue.heap == [10, 15]
    priority_queue.insert(20)
    assert priority_queue.heap == [10, 15, 20]
    priority_queue.insert(0)
    assert priority_queue.heap == [0, 10, 20, 15]
    priority_queue.insert(30)
    assert priority_queue.heap == [0, 10, 20, 15, 30]
    priority_queue.pull()
    assert priority_queue.heap == [10, 15, 20, 30]
    priority_queue.pull()
    assert priority_queue.heap == [15, 30, 20]
    priority_queue.insert(2)
    assert priority_queue.heap == [2, 15, 20, 30]
    priority_queue.insert(4)
    assert priority_queue.heap == [2, 4, 20, 30, 15]
    priority_queue.insert(-1)
    assert priority_queue.heap == [-1, 4, 2, 30, 15, 20]
    priority_queue.insert(-3)
    assert priority_queue.heap == [-3, 4, -1, 30, 15, 20, 2]


if __name__ == "__main__":
    main()


class Node:

    def __init__(self, priority, value=None):
        self.priority = priority
        self.value = value

    def __eq__(self, other):
        return (self.priority == other.priority) and (self.value == other.value)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.value < other.value
        else:
            return self.priority < other.priority

    def __le__(self, other):
        return (self < other) or (self == other)

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)

    def __repr__(self):
        if self.value is None:
            return f"({self.priority})"
        return f"({self.value}: {self.priority})"
