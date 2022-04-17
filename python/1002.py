import math

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

        if abs(r1 - r2) > distance:
            print(0)
        elif abs(r1 - r2) == distance:
            if r1 == r2:
                print(-1)
            else:
                print(1)
        elif abs(r1 - r2) < distance < (r1 + r2):
            print(2)
        elif (r1 + r2) == distance:
            print(1)
        elif (r1 + r2) < distance:
            print(0)