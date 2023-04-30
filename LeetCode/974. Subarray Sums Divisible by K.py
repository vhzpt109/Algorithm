from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cml_sums = []
        tmp_sum = 0
        for num in nums:
            tmp_sum += num
        cml_sums.append(tmp_sum)

        table = {}
        count = 0
        table[0] = [-1]
        for idx, cml_sum in enumerate(cml_sums):
            target = cml_sum % k
            if target in table:
                count += 1

            if cml_sum not in table:
                table[cml_sum] = [idx]
            else:
                table[cml_sum].append(idx)

        return count