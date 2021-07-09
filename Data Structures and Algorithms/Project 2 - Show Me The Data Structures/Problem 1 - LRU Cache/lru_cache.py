from __future__ import annotations
from typing import Any
from queue import Queue

class LRU_Cache:
    """Implementation of a Last Recently Used (LRU) Cache.

    The idea of an LRU Cache is to maintain a cache of a fixed size while still being able to add elements.
    When the cache is at capacity and a new element is added, the least recently used element is removed to make room.
    This implementation uses a hashmap to hold the elements for O(1) lookup and a queue to keep track of the recency of use.

    Attributes:
        _capacity (int): The maximum size of the cache.
        _size (int): The number of elements in the cache.
        _queue (Queue): A queue of the elements tracking recency.
        _cache (dict): A hashmap holding the nodes of the queue.
    """

    def __init__(self: int, capacity: int):
        """The constructor for the LRU Cache class.

        Parameters:
            _capacity (int): The maximum size of the cache.
            _size (int): The number of elements in the cache.
            _queue (Queue): A queue of the elements tracking recency.
            _cache (dict): A hashmap holding the nodes of the queue.
        """
        self._capacity = capacity
        self._size = 0
        self._queue = Queue()
        self._cache = dict()

    def __str__(self) -> str:
        """Represents the LRU Cache as a string.

        Note that this prints the key value pairs in the cache in the order of the built-in dict class,
        not in the order of the queue.
        
        Returns:
            str: A string representing the LRU Cache.
        """
        return "{" + str(", ".join([f"{key}: {self._cache[key].value}" for key in self._cache]) + "}")

    def set(self, key: Any, value: Any):
        """Add or modify a key value pair in the cache.

        If the key is already in the cache, update the value. Otherwise, add the key value pair to the cache.

        Parameters:
            key (Any): The immutable key used to access a value.
            value (Any): A mutable value associated with a key.
        """
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
        """Access the value of a given key.

        If the key is not in the cache, this returns -1 as specified in the assignment.
        There is currently no distinction between a value of -1 and a failure to find a key,
        though it would be easy to make this throw a KeyError exception like the dict class.

        Parameters:
            key (Any): The immutable key used to access a value.
        
        Returns:
            Any: The value associated with the given key or -1 if the key was not found in the cache.
        """
        if key not in self._cache:
            return -1

        self._cache[key] = self._queue.requeue(self._cache[key])
        return self._cache[key].value
