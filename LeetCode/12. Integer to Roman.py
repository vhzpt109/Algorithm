class Solution:
    def intToRoman(self, num: int) -> str:
        hash_table = {
            1: "I",
            4: "IV", 5: "V",
            9: "IX", 10: "X",
            40: "XL", 50: "L",
            90: "XC", 100: "C",
            400: "CD", 500: "D",
            900: "CM", 1000: "M"
        }

        result = ''
        for n in hash_table.keys().__reversed__():
            while n <= num:
                result += hash_table[n]
                num -= n

        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.intToRoman(58))
    print(obj.intToRoman(1994))
