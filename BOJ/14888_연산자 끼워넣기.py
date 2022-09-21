def backtracking(an_list, variable, depth, operator_list):
    global result_list
    for i in range(len(operator_list)):
        temp = variable
        if operator_list[i] > 0:
            operator_list[i] -= 1
            if i == 0:
                variable += an_list[depth]
            elif i == 1:
                variable -= an_list[depth]
            elif i == 2:
                variable *= an_list[depth]
            elif i == 3:
                if variable >= 0:
                    variable //= an_list[depth]
                else:
                    variable = (-variable // an_list[depth]) * -1
            if depth == len(an_list) - 1:
                result_list.append(variable)
                operator_list[i] += 1
                return
            backtracking(an_list, variable, depth + 1, operator_list)
            operator_list[i] += 1
            variable = temp


if __name__ == "__main__":
    n = int(input())
    an_list = list(map(int, input().split()))
    operator_list = list(map(int, input().split()))

    result_list = []
    backtracking(an_list, an_list[0], 1, operator_list)

    print(max(result_list))
    print(min(result_list))