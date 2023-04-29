class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_table = {}
        word_table = {}

        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        for idx, c in enumerate(pattern):
            word = words[idx]
            if c not in char_table:
                if word in word_table:
                    return False
                else:
                    char_table[c] = word
                    word_table[word] = c
            else:
                if char_table[c] != word:
                    return False
        return True