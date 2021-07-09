from __future__ import annotations
from typing import Any
from typing import Union

class Queue:
    """A first-in-first-out queue represented as a doubly linked list.

    Attributes:
        head (Node): The first element in the queue, next to be removed.
        tail (Node): The last element in the queue, most recently added.
    """

    def __init__(self):
        """The constructor for the Queue class."""
        self.head = None
        self.tail = None

    def enqueue(self, value: Any) -> Node:
        """Add an element onto the end of the queue.
        
        Parameters:
            value (Any): The value to be added to the queue.

        Returns:
            Node: A node containing the given value at the end of the queue.
        """
        cur = Node(value)

        if self.head is None:
            self.head = cur
        if self.tail is not None:
            self.tail.next = cur
            cur.prev = self.tail
        self.tail = cur
        return cur

    def dequeue(self) -> Union[Node, None]:
        """Remove the tail from the queue.

        Returns:
            Node/None: The value of the removed tail if the queue was not empty. Otherwise, None.
        """
        if self.head is None:
            return None

        value = self.head.value
        self.head = self.head.next
        self.head.prev = None
        return value

    def requeue(self, node: Node) -> Node:
        """Remove the given node from the queue and then add it again as the tail.

        Parameters:
            node (Node): The node to be requeued.

        Returns:
            Node: The node after being requeued.
        """
        if node is self.head:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node is self.tail:
            self.tail = node.next
        else:
            node.next.prev = node.prev

        return self.enqueue(node.value)


class Node:
    """The nodes of the doubly linked list.
    
    Attributes:
        value (Any): The value of the node.
        next (Node): The node before the current node in the linked list.
        prev (Node): The node after the current node in the linked list.
    """

    def __init__(self, value: Any):
        """The constructor for the Node class.

        Parameters:
            value (Any): The value of the node.
        """
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        """Represent the Node as a string.
        
        Returns:
            str: A string representing the node.
        """
        return self.value
