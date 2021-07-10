import sys
from typing import Generator
from priority_queue import Priority_Queue
from node import Node

def main():
    """Test the Huffman Coding implementation.

    Huffman Coding is a lossless data compression algorithm that assigns bitstrings to a symbol based on frequency,
    therefore making it so that the most common symbols take up the least amount of space.
    This implementation uses a priority queue to build the huffman tree for encoding as well as a dictionary for decoding.

    This implementation is purely intended to demonstrate the huffman coding algorithm as well as a priority queue implementation.
    On small inputs like the one demonstrated below, this implementation actually increases memory use because of the size
    of the dictionary, though it does effectively compress data larger than a kilobyte (half a page of text).
    If this were to be optimized, the decode table would be the best place to start.
    """

    a_great_sentence = "The bird is the word"
    print(f"The size of the data is: {sys.getsizeof(a_great_sentence)}")
    print(f"The content of the data is: {a_great_sentence}")

    encoded_data, decode_table = huffman_encoding(a_great_sentence)

    print(f"The size of the encoded data is: {sys.getsizeof(encoded_data)}")
    print(f"The content of the encoded data is: {format(encoded_data, 'b')}")

    decoded_data = huffman_decoding(encoded_data, decode_table)

    print(f"The size of the decoded data is: {sys.getsizeof(decoded_data)}")
    print(f"The content of the encoded data is: {decoded_data}")

def huffman_encoding(data: str) -> tuple[int, dict[str, str]]:
    frequency_table = symbol_frequency(data)
    tree = build_huffman_tree(frequency_table)
    encoded_data, decode_table = encode_data(data, tree)
    return encoded_data, decode_table

def symbol_frequency(data: str) -> dict[str, int]:
    frequency_table = {}
    for symbol in data:
        if symbol in frequency_table:
            frequency_table[symbol] += 1
        else:
            frequency_table[symbol] = 1
    return frequency_table

def build_huffman_tree(frequency_table: dict[str, int]) -> Node:
    priority_queue = Priority_Queue()
    for symbol in frequency_table:
        priority_queue.insert(Node(priority=frequency_table[symbol], symbol=symbol))

    while len(priority_queue) > 1:
        left_child = priority_queue.pull()
        right_child = priority_queue.pull()
        combined_priority = left_child.priority + right_child.priority
        priority_queue.insert(Node(priority=combined_priority, left_child=left_child, right_child=right_child))
    return priority_queue.pull()

def encode_data(data: str, tree: Node) -> tuple[int, dict[str, str]]:
    encode_table = {}
    decode_table = {}
    encoded_data = ''
    for symbol, code in end_nodes(tree):
        encode_table[symbol] = code
        decode_table[code] = symbol
    for symbol in data:
        encoded_data += encode_table[symbol]
    return int(encoded_data, base=2), decode_table

def end_nodes(tree: Node) -> Generator[tuple[str, str], None, None]:
    queue = [(tree, '')]
    while len(queue) > 0:
        node, code = queue.pop()
        if node.left_child is None and node.right_child is None:
            yield node.symbol, code
        if node.left_child is not None:
            queue.append((node.left_child, code + '0'))
        if node.right_child is not None:
            queue.append((node.right_child, code +'1'))

def huffman_decoding(encoded_data: int, decode_table: dict[str, str]) -> str:
    return ''.join((symbol) for symbol in extract_symbols(format(encoded_data, 'b'), decode_table))

def extract_symbols(encoded_data: str, decode_table: dict[str, str]) -> Generator[str, None, None]:
    current_symbol = ''
    for bit in encoded_data:
        current_symbol += bit
        if current_symbol in decode_table:
            yield decode_table[current_symbol]
            current_symbol = ''


if __name__ == "__main__":
    main()
