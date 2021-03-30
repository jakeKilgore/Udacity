import sys
from priority_queue import Priority_Queue
from node import Node

def main():
    a_great_sentence = "The bird is the word"
    print(f"The size of the data is: {sys.getsizeof(a_great_sentence)}")
    print(f"The content of the data is: {a_great_sentence}")

    encoded_data, decode_table = huffman_encoding(a_great_sentence)

    print(f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
    print(f"The content of the encoded data is: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, decode_table)

    print(f"The size of the decoded data is: {sys.getsizeof(decoded_data)}")
    print(f"The content of the encoded data is: {decoded_data}")

def huffman_encoding(data):
    frequency_table = symbol_frequency(data)
    tree = build_huffman_tree(frequency_table)
    encoded_data, decode_table = encode_data(data, tree)
    return encoded_data, decode_table

def symbol_frequency(data):
    frequency_table = {}
    for symbol in data:
        if symbol in frequency_table:
            frequency_table[symbol] += 1
        else:
            frequency_table[symbol] = 1
    return frequency_table

def build_huffman_tree(frequency_table):
    priority_queue = Priority_Queue()
    for symbol in frequency_table:
        priority_queue.insert(Node(priority=frequency_table[symbol], symbol=symbol))

    while len(priority_queue) > 1:
        left_child = priority_queue.pull()
        right_child = priority_queue.pull()
        combined_priority = left_child.priority + right_child.priority
        priority_queue.insert(Node(priority=combined_priority, left_child=left_child, right_child=right_child))
    return priority_queue.pull()

def encode_data(data, tree):
    encode_table = {}
    decode_table = {}
    encoded_data = ''
    for symbol, code in end_nodes(tree):
        encode_table[symbol] = code
        decode_table[code] = symbol
    for symbol in data:
        encoded_data += encode_table[symbol]
    return encoded_data, decode_table

def end_nodes(tree):
    queue = [(tree, '')]
    while len(queue) > 0:
        node, code = queue.pop()
        if node.left_child is None and node.right_child is None:
            yield node.symbol, code
        if node.left_child is not None:
            queue.append((node.left_child, code + '0'))
        if node.right_child is not None:
            queue.append((node.right_child, code +'1'))

def huffman_decoding(encoded_data, decode_table):
    return ''.join((symbol) for symbol in extract_symbols(encoded_data, decode_table))

def extract_symbols(encoded_data, decode_table):
    current_symbol = ''
    for bit in encoded_data:
        current_symbol += bit
        if current_symbol in decode_table:
            yield decode_table[current_symbol]
            current_symbol = ''

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
