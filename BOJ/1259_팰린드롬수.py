if __name__ == "__main__":
    while True:
        n = list(input())
        if int(n[0]) == 0:
            break
        elif n[:] == n[::-1]:
            print("yes")
        else:
            print("no")