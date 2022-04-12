if __name__ == "__main__":
    n = int(input())

    list = []

    for _ in range(n):
        list.append(int(input()))
    list.sort()

    for number in list:
        print(number)