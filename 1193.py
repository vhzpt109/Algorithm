if __name__ == "__main__":
    x = int(input())

    max_number = 1
    index_range = 1
    while x > index_range:
        max_number += 1
        index_range += max_number

    numerator = -1
    denominator = -1
    diff = index_range - x
    if max_number % 2 != 0:
        numerator = 1 + diff
        denominator = max_number - diff
    else:
        numerator = max_number - diff
        denominator = 1 + diff

    print(str(numerator) + "/" + str(denominator))