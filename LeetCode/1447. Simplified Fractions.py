from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        hash_table = {}
        result = []
        for numerator in range(1, n + 1):
            for denominator in range(numerator + 1, n + 1):
                if numerator / denominator not in hash_table:
                    hash_table[numerator / denominator] = 1
                    result.append(f"{numerator}/{denominator}")
        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.simplifiedFractions(2))