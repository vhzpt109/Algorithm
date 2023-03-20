permutations_list = []


def dfs(_list, residual_list):
    global permutation_list
    if len(residual_list) == 0:
        permutations_list.append(_list[:])
        return

    for i, residual in enumerate(residual_list):
        clone_residual_list = residual_list[:]
        del clone_residual_list[i]
        _list.append(residual)
        dfs(_list, clone_residual_list)
        _list.pop()


def makePermutations(_list):
    dfs([], _list)


if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    makePermutations(input_list)

    print(permutations_list)