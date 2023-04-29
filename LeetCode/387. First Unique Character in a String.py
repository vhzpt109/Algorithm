class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_hash_table = {}
        for c in s:
            count = count_hash_table.get(c)
            if count is None:
                count_hash_table[c] = 1
                continue

            count_hash_table[c] += 1

        for idx, c in enumerate(s):
            if count_hash_table[c] == 1:
                return idx

        return -1