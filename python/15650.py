from itertools import combinations

if __name__ == "__main__":
    n, m = map(int, input().split())

    n_range = [i for i in range(1, n + 1)]

    combination_list = list(combinations(n_range, m))
    combination_list.sort()

    for combination in combination_list:
        for i in range(len(combination)):
            print(combination[i], end=" ")
        print()