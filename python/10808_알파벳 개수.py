if __name__ == "__main__":
    s = sorted(input())

    count = [0] * 26

    for char in s:
        count[ord(char) - 97] += 1

    print(*count)