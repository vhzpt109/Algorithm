class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        result = ''
        carry = i = 0
        l1, l2 = len(num1), len(num2)
        l3 = max(l1, l2)
        while i < l3 or carry:
            digit1 = int(num1[i]) if i < l1 else 0
            digit2 = int(num2[i]) if i < l2 else 0
            sum_digit = (digit1 + digit2 + carry) % 10
            carry = (digit1 + digit2 + carry) // 10
            result += str(sum_digit)
            i += 1
        return result[::-1]