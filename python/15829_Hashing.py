if __name__ == "__main__":
    l = int(input())
    s = input()

    hash = 0
    for i in range(len(s)):
        hash += (ord(s[i]) - 96) * (31**i)
    print(hash % 1234567891)