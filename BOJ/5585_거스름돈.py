if __name__ == "__main__":
    pay = 1000 - int(input())

    money_list = [500, 100, 50, 10, 5, 1]

    count = 0
    for money in money_list:
        if pay >= money:
            count += pay // money
            pay = pay % money
    print(count)