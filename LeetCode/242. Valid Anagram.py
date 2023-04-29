class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table = {}
        for c in s:
            match_idx = hash_table.get(c)
            if match_idx is None:
                hash_table[c] = 1
                continue
            hash_table[c] += 1

        for c in t:
            match_idx = hash_table.get(c)
            if match_idx is None:
                return False
            hash_table[c] -= 1

        for key, value in hash_table.items():
            if value != 0:
                return False
        return True