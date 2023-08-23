class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_table = {}

        max_len = 0
        start = 0
        for end, c in enumerate(s):
            if c in hash_table and start <= hash_table[c]:
                start = hash_table[c] + 1
            else:
                max_len = max(max_len, end - start + 1)
            hash_table[c] = end

        return max_len


if __name__ == "__main__":
    obj = Solution()
    print(obj.lengthOfLongestSubstring("abcabcbb"))
    print(obj.lengthOfLongestSubstring("bbbbb"))
    print(obj.lengthOfLongestSubstring("pwwkew"))
    print(obj.lengthOfLongestSubstring(" "))