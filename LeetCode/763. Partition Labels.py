from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idxs = {}
        for idx, c in enumerate(s):
            last_idxs[c] = idx

        partitions = []
        temp_idx = 0
        partition_start = 0

        for idx, c in enumerate(s):
            last_idx = last_idxs[c]
            temp_idx = max(temp_idx, last_idx)
            if idx == temp_idx:
                partitions.append(len(s[partition_start:idx + 1]))
                partition_start = idx + 1

        return partitions


if __name__ == "__main__":
    obj = Solution()
    s = "ababcbacadefegdehijhklij"
    print(obj.partitionLabels(s))