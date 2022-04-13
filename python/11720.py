if __name__ == "__main__":
    n = int(input())
    s = list(input())
    if len(s) != n:
        exit()

    sum = 0
    for i in s:
        sum += int(i)
    print(sum)