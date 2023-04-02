bracket_dict = {
    "(": ")",
    "[": "]"
}

bracket_number = {
    "(": 2,
    "[": 3
}

if __name__ == "__main__":
    _string = input().rstrip()

    bracket_sum = 0
    bracket_sub_sum = 1
    stack = []
    for char in _string:
        if char in bracket_dict.keys():
            stack.append(char)
            bracket_sub_sum *= bracket_number[char]
        elif char in bracket_dict.values():
            value = stack.pop()
            if char != bracket_dict[value]:
                print(0)
                exit(0)
            else:
                bracket_sum += bracket_sub_sum
                bracket_sub_sum //= bracket_number[value]

    print(bracket_sum)