if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())

    abc = list(str(a * b * c))
    numbers = [0] * 10

    for i in abc:
        numbers[int(i)] += 1

    for number in numbers:
        print(number)