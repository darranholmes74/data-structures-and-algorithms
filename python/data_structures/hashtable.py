class Hashtable:
    def __init__(self, size=1024):
        self._size = size
        self._buckets = size * [None]

    def set(self, key, value):
        # TODO: Hash the key
        h = self.hash(key)

        found = False
        for k, v in enumerate(self._buckets[h] or []):
            if v[0] == key:
                self._buckets[h][k] = (key, value)
                found = True
                break
        if not found:
            self._buckets[h] = self._buckets[h] or []
            self._buckets[h].append((key, value))

    def get(self, key):
        # TODO: Hash the key
        h = self.hash(key)
        for k, v in self._buckets[h] or []:
            if k == key:
                return v
        return None

    def has(self, key):
        # TODO: Hash the key
        h = self.hash(key)
        for k, v in self._buckets[h] or []:
            if k == key:
                return True
        return False

    def keys(self):
        keys = []
        for bucket in self._buckets:
            if bucket:
                for k, v in bucket:
                    keys.append(k)
        return keys

    def hash(self, key):
        hash_total = 0
        for char in key:
            hash_total += ord(char)
        primed_number = hash_total * len(key) * 19
        index = primed_number % self._size
        return index
