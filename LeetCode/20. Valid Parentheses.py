class Solution:
    def isValid(self, s: str) -> bool:
        hash_table = {'(': ')', '{': '}', '[': ']'}

        stack = []
        for c in s:
            if c in hash_table:
                stack.append(c)
            elif len(stack) == 0 or hash_table[stack.pop()] != c:
                return False

        return len(stack) == 0


if __name__ == "__main__":
    obj = Solution()
    print(obj.isValid("()"))