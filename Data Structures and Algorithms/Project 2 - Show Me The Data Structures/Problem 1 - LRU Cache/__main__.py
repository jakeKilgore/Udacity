from lru_cache import LRU_Cache

def main():
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    assert(our_cache.get(1) == 1)       # returns 1
    assert(our_cache.get(2) == 2)       # returns 2
    assert(our_cache.get(9) == -1)      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    assert(our_cache.get(3) == -1)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


if __name__ == "__main__":
    main()
