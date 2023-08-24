from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        for i, c in enumerate(shortest):
            for other in strs:
                if other[i] != c:
                    return shortest[:i]
        return shortest


if __name__ == "__main__":
    obj = Solution()
    print(obj.longestCommonPrefix(["flower", "flow", "flight"]))
