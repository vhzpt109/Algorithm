if __name__ == "__main__":
    alphabet_list = list(input())
    number_list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

    cost = 0

    for number in alphabet_list:
        cost += (number_list.index([_ for _ in number_list if number in _][0]) + 3)

    print(cost)