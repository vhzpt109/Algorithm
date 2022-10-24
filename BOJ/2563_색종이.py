if __name__ == "__main__":
    n = int(input())

    confetti = [[0 for _ in range(101)] for _ in range(101)]
    for _ in range(n):
        x, y = map(int, input().split())

        for col in range(x, x + 10):
            for row in range(y, y + 10):
                confetti[col][row] = 1

    count = 0
    for row in confetti:
        count += row.count(1)
    print(count)