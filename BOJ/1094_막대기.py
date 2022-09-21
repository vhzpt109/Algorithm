if __name__ == "__main__":
    x = int(input())
    count = 0
    while x != 0:
        if x % 2 == 1:
            count += 1
        x = x // 2
    print(count)