class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_hash_table = {}

        for word in words:
            match_word = words_hash_table.get(word)
            if match_word is None:
                words_hash_table[word] = 1
            else:
                words_hash_table[word] += 1

        word_list = list(words_hash_table.items())
        word_list.sort()
        word_list.sort(reverse=True, key=lambda value: value[1])

        output = []
        for i in range(k):
            output.append(word_list[i][0])
        return output