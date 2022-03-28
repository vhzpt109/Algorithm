if __name__ == '__main__':
    number = list(map(int, input().split()))
    number.sort()

    number_set = set(number)

    if len(number_set) == 1:
        print(10000 + number[0] * 1000)
    elif len(number_set) == 2:
        print(1000 + number[1] * 100)
    elif len(number_set) == 3:
        print(number[-1] * 100)