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

    ccw1 = get_ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = get_ccw(x1, y1, x2, y2, x4, y4)