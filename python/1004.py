if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        x1, y1, x2, y2 = list(map(int, input().split()))

        n = int(input())
        count = 0
        for _ in range(n):
            x, y, r = map(int, input().split())
            dis1 = (x1 - x)**2 + (y1 - y)**2
            dis2 = (x2 - x)**2 + (y2 - y)**2
            pow_r = r**2

            if pow_r > dis1 and pow_r > dis2:
                pass
            elif pow_r > dis1:
                count += 1
            elif pow_r > dis2:
                count += 1

        print(count)