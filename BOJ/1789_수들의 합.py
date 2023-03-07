if __name__ == "__main__":
    s = int(input())

    _sum = 0
    n = 0
    i = 1
    while True:
        _sum += i
        n += 1
        if _sum == s:
            break
        elif _sum > s:
            _sum -= (i + i + 1)
            n -= 1
            break
        else:
            i += 1
    print(n)