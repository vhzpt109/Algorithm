from string import ascii_lowercase

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_table = {}
        for alphabet in ascii_lowercase:
            hash_table[alphabet] = -1

        max_len = 0
        start, end = 0, -1
        p1, p2 = 0, 0
        while p2 < len(s) - 1:
            if hash_table[s[p2]] == -1:
                hash_table[s[p2]] = p2
                end = p2
                p2 += 1

            elif hash_table[s[p2]] != -1:
                if p1 >= hash_table[s[p2]]:
                    p1 = hash_table[s[p2]] + 1
                    start = p1
                else:
                    p2 += 1

            max_len = max(max_len, end - start + 1)

        return max_len


if __name__ == "__main__":
    obj = Solution()
    print(obj.lengthOfLongestSubstring("abcadd"))