if __name__ == "__main__":
    h, m = map(int, input().split())
    if m > 45:
        m = m - 45
        print(h, m)
    else:
        if h == 0:
            h = 23
        else:
            h = h - 1
        m = 15 + m
        print(h, m)