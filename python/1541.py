if __name__ == "__main__":
    expression = input()
    total = 0

    minus_split_expression = expression.split("-")
    add_split_expression = minus_split_expression[0].split("+")
    for add_split in add_split_expression:
        total += int(add_split)

    for minus_split in minus_split_expression[1:]:
        add_split_expression = minus_split.split("+")
        if len(add_split_expression) > 1:
            add_sum = 0
            for add_split in add_split_expression:
                add_sum += int(add_split)
            total -= add_sum
        else:
            total -= int(add_split_expression[0])

    print(total)