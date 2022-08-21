if __name__ == "__main__":
    s = list(input())

    if s == s[::-1]:
        print(1)
    else:
        print(0)