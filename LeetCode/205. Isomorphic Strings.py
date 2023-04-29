class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_table1 = {}
        hash_table2 = {}
        for idx in range(len(s)):
            match1 = hash_table1.get(s[idx])
            match2 = hash_table2.get(t[idx])
            if match1 is None and match2 is None:
                hash_table1[s[idx]] = t[idx]
                hash_table2[t[idx]] = s[idx]
                continue
            elif match1 == t[idx] and match2 == s[idx]:
                continue

            return False

        return True