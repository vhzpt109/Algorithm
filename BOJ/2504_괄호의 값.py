bracket_dict = {
    "(": ")",
    "[": "]"
}

bracket_dict_by_value = {
    ")": "(",
    "]": "["
}

bracket_number = {
    "(": 2,
    "[": 3
}

if __name__ == "__main__":
    _string = input()

    bracket_sum = 0
    bracket_sub_sum = 1
    stack = []
    for i in range(len(_string)):
        if _string[i] in bracket_dict.keys():
            stack.append(_string[i])
            bracket_sub_sum *= bracket_number[_string[i]]

        elif _string[i] in bracket_dict.values():
            if not stack or bracket_dict[stack[-1]] != _string[i]:
                print(0)
                exit(0)
            if _string[i - 1] == bracket_dict_by_value[_string[i]]:
                bracket_sum += bracket_sub_sum
            stack.pop()
            bracket_sub_sum //= bracket_number[bracket_dict_by_value[_string[i]]]
    if stack:
        print(0)
    else:
        print(bracket_sum)