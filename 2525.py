if __name__ == "__main__":
    h, m = map(int, input().split())
    cooking_time = int(input())
    if m + cooking_time > 59:
        h = h + (m + cooking_time) // 60
        if h > 23:
            h = h - 24
        m = (m + cooking_time) % 60
        print(h, m)
    else:
        m = m + cooking_time
        print(h, m)