from queue import Queue

class LRU_Cache:

    def __init__(self: int, capacity: int):
        self._capacity = capacity
        self._size = 0
        self._queue = Queue()
        self._cache = dict()

    def __str__(self) -> str:

        return "{" + str(", ".join([f"{key}: {self._cache[key].value}" for key in self._cache]) + "}")

    def set(self, key: Any, value: Any):
        if key in self._cache:
            self._cache[key] = self._queue.requeue(self._cache[key])
            self._cache[key].value = value
            return

        if self._size >= self._capacity:
            oldest = self._queue.dequeue()
            self._cache.pop(oldest)
        else:
            self._size += 1
        self._cache[key] = self._queue.enqueue(key)
        self._cache[key].value = value

    def get(self, key: Any) -> Any:

        if key not in self._cache:
            return -1

        self._cache[key] = self._queue.requeue(self._cache[key])
        return self._cache[key].value
