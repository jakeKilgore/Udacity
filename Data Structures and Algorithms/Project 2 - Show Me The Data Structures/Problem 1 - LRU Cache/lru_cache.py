from queue import Queue

class LRU_Cache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self._cache = dict()
        self._nodes = dict()
        self._queue = Queue()

    def __str__(self):
        return "{" + str(", ".join([f"{key}: {self._cache[key]}" for key in self._cache]) + "}")

    def set(self, key, value):
        if key in self._cache:
            self._nodes[key] = self._queue.requeue(self._nodes[key])
            self._cache[key] = value
            return

        if self.size == self.capacity:
            oldest = self._queue.dequeue()
            self._cache.pop(oldest)
        else:
            self.size += 1
        self._nodes[key] = self._queue.enqueue(key)
        self._cache[key] = value

    def get(self, key):
        if key not in self._cache:
            return -1

        self._nodes[key] = self._queue.requeue(self._nodes[key])
        return self._cache[key]
