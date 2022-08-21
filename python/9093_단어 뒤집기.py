if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        word_list = list(map(str, input().split(' ')))
        for word in word_list:
            print(word[::-1], end=" ")
        print()