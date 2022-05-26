from itertools import permutations

if __name__ == "__main__":
    n, m = map(int, input().split())

    n_range = [i for i in range(1, n + 1)]

    permutation_list = list(permutations(n_range, m))
    permutation_list.sort()

    for permutations in permutation_list:
        for i in range(len(permutations)):
            print(permutations[i], end=" ")
        print()