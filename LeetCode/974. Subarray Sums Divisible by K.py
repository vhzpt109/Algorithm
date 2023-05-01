class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cml_sums = []
        tmp_sum = 0
        for num in nums:
            tmp_sum += num
            cml_sums.append(tmp_sum % k)

        hash_table = {}
        count = 0
        hash_table[0] = [-1]
        for idx, cml_sum in enumerate(cml_sums):
            target = cml_sum
            if target in hash_table:
                count += len(hash_table[target])

            if target not in hash_table:
                hash_table[target] = [idx]
            else:
                hash_table[target].append(idx)

        return count