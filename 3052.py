if __name__ == "__main__":
    numbers = []
    for i in range(10):
        numbers.append(int(input()))
    numbers_remainder = []

    for i in range(len(numbers)):
        numbers_remainder.append(numbers[i] % 42)

    numbers_deduplication = set(numbers_remainder)
    print(len(numbers_deduplication))