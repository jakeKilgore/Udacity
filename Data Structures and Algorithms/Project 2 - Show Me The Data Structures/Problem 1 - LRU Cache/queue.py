class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        cur = Node(value)

        if self.head is None:
            self.head = cur
        if self.tail is not None:
            self.tail.next = cur
            cur.prev = self.tail
        self.tail = cur
        return cur
    
    def dequeue(self):
        if self.head is None:
            return None

        value = self.head.value
        self.head = self.head.next
        self.head.prev = None
        return value
    
    def requeue(self, node):
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

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
