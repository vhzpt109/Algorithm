import random
from typing import List


class RandomizedSet:
    def __init__(self):
        self._table = {}
        self._arry = []

    def insert(self, val: int) -> bool:
        idx = self._table.get(val)
        if idx is not None:
            return False

        idx = len(self._arry)
        self._arry.append(val)
        self._table[val] = idx
        return True

    def remove(self, val: int) -> bool:
        idx = self._table.get(val)
        if idx is None:
            return False

        last_val = self._arry[-1]
        self._arry[idx] = last_val
        self._table[last_val] = idx
        self._arry.pop()
        self._table.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(self._arry)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()