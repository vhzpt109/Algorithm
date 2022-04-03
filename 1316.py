if __name__ == "__main__":
    n = int(input())

    group_word_cnt = n

    for _ in range(n):
        word = input()
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                continue
            elif word[i] in word[i + 1:]:
                group_word_cnt -= 1
                break

    print(group_word_cnt)