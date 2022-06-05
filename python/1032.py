if __name__ == "__main__":
    n = int(input())
    word = list(input())

    for i in range(n - 1):
        temp_words = list(input())
        for j in range(len(word)):
            if word[j] != temp_words[j]:
                word[j] = '?'

    print(''.join(word))