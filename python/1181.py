import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    word_list = []
    for _ in range(n):
        word_list.append(sys.stdin.readline().strip())
    word_list = list(set(word_list)) # remove overlap
    word_list.sort()
    word_list.sort(key=len)

    for word in word_list:
        print(word)