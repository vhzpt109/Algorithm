if __name__ == "__main__":
    abcd = list(map(int, input().split()))
    abcd.sort()

    print(abcd[0] * abcd[2])