if __name__ == "__main__":
    n = int(input())
    word_list = [list(input()) for _ in range(n)]
    word_list.sort(key=len, reverse=True)

    alphabet_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0,
                     'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
    for word in word_list:
        for i, alphabet in enumerate(word):
            alphabet_dict[alphabet] += 10**(len(word) - i - 1)

    alphabet_dict = sorted(alphabet_dict.items(), key=lambda item: item[1], reverse=True)

    _sum = 0
    for i in range(10):
        _sum += alphabet_dict[i][1] * (9 - i)
    print(_sum)