class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = dict()
        self.cap = capacity
        self.queue = []

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        item = self.cache[key] if key in self.cache else -1

        if item != -1:
            self.queue.remove(key)
            self.queue.insert(0, key)

        return item

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.

        if key in self.cache:
            self.queue.remove(key)
        elif len(self.queue) == self.cap:
            lru = self.queue.pop()
            del(self.cache[lru])

        self.cache[key] = value
        self.queue.insert(0, key)

def test(cap = 100):
    lc = LRU_Cache(cap)

    #Fill cache to capacity
    for i in range(cap):
        lc.set(i, i)
    #Check all but last item
    for i in range(cap - 1):
        lc.get(i)

    full_cache_size = len(lc.queue)
    #Test 1 Add to full cache
    lc.set(cap, cap)
    if cap == lc.get(cap):
        print(lc.get(cap))  #expected output: 100
        print("Pass - able to add number to full cache")
    else:
        print("Fail")

    #Test 2 lru removal
    if lc.get(cap - 1) == - 1:
        print(lc.get(cap - 1)) # expected ouput: -1
        print("Pass - lru item was removed ")
    else:
        print("Fail")

    #Test 3 cache size remained the same after additions
    for i in range(cap + 1, cap * 2):
        lc.set(i, i)

    if full_cache_size == len(lc.queue):
        print(len(lc.queue)) # expected output 100
        print("Pass - cache remained the same size")
    else:
        print("Fail")

if __name__ == "__main__":
    test()
