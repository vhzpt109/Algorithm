if __name__ == "__main__":
    side = list(map(int, input().split()))
    while side[0] != side[1] != side[2] != 0:
        side.sort()
        if side[0]**2 + side[1]**2 == side[2]**2:
            print("right")
        else:
            print("wrong")
        side = list(map(int, input().split()))