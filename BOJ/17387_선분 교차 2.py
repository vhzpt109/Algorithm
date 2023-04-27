def get_ccw(x1, y1, x2, y2, x3, y3):
    v = ((x1 * y2) + (x2 * y3) + (x3 * y1)) - ((x2 * y1) + (x3 * y2) + (x1 * y3))

    if v > 0:
        return 1
    elif v == 0:
        return 0
    else:
        return -1


if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    ccw123 = get_ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = get_ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = get_ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = get_ccw(x3, y3, x4, y4, x2, y2)

    mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)

    if ccw123 * ccw124 == 0 and ccw341 * ccw342 == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            print(1)
        else:
            print(0)
    else:
        if ccw123 * ccw124 <= 0 and ccw341 * ccw342 <= 0:
            print(1)
        else:
            print(0)