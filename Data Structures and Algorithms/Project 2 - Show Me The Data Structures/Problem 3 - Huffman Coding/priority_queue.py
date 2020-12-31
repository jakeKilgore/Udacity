class Priority_Queue:

    def __init__(self):
        self.heap = []

    def __repr__(self):
        return str(self.heap)

    def __len__(self):
        return len(self.heap)

    def get_left_child_index(self, parent_index):
        return int(2 * parent_index + 1)

    def get_right_child_index(self, parent_index):
        return int(2 * parent_index + 2)

    def get_parent_index(self, child_index):
        return int((child_index - 1) / 2)

    def get_smallest_child_index(self, parent_index):
        left_child = self.get_left_child_index(parent_index)
        right_child = self.get_right_child_index(parent_index)
        if not self.has_left_child(parent_index):
            assert not self.has_right_child(parent_index), "There are gaps in the heap."
            raise IndexError("Trying to compare children of childless node.")
        if not self.has_right_child(parent_index) or self.heap[left_child] < self.heap[right_child]:
            return left_child
        else:
            return right_child

    def has_left_child(self, parent_index):
        return self.get_left_child_index(parent_index) < len(self.heap)

    def has_right_child(self, parent_index):
        return self.get_right_child_index(parent_index) < len(self.heap)

    def pull(self):
        assert len(self.heap) != 0, "Trying to fetch min from empty queue."
        min_node = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_node

    def insert(self, node):
        self.heap.append(node)
        self.heapify_up(len(self.heap) - 1)

    def heapify_down(self, index):
        try:
            smallest_child_index = self.get_smallest_child_index(index)
        except IndexError:
            return
        if self.heap[smallest_child_index] > self.heap[index]:
            return
        self.heap[index], self.heap[smallest_child_index] = self.heap[smallest_child_index], self.heap[index]
        self.heapify_down(smallest_child_index)

    def heapify_up(self, index):
        if index == 0:
            return
        parent_index = self.get_parent_index(index)
        if self.heap[parent_index] < self.heap[index]:
            return
        self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
        self.heapify_up(parent_index)
