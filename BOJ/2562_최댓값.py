if __name__ == "__main__":
    numbers = []
    for _ in range(9):
        numbers.append(int(input()))
    print(max(numbers))
    print(numbers.index(max(numbers)) + 1)