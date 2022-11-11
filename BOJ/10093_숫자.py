if __name__ == "__main__":
    ab = list(map(int, input().split()))
    ab.sort()

    if ab[0] == ab[1] or ab[0] + 1 == ab[1]:
        print(0)
    else:
        print(ab[1] - ab[0] - 1)

    for i in range(ab[0] + 1, ab[1]):
        print(i, end=" ")