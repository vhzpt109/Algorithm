from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}

        for word in strs:
            word_sorted = ''.join(sorted(word))
            if hash_table.get(word_sorted):
                hash_table[word_sorted].append(word)
            else:
                hash_table[word_sorted] = [word]

        return list(hash_table.values())


if __name__ == "__main__":
    obj = Solution()
    print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))