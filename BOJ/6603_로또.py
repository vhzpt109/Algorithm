def dfs(combination, number_list, visited_number):
    if len(combination) == 6:
        print(*combination)
        return

    visited_number_clone = visited_number[:]
    for i in range(len(visited_number_clone)):
        if not visited_number_clone[i]:
            visited_number_clone[i] = True
            combination.append(number_list[i])
            dfs(combination, number_list, visited_number_clone)
            combination.pop()


if __name__ == "__main__":
    while True:
        t = list(map(int, input().split()))
        if t[0] == 0: break
        number_list = t[1:]
        visited_number = [False for _ in range(len(number_list))]

        dfs([], number_list, visited_number)
        print()
