from itertools import combinations

if __name__ == "__main__":
    n, k = map(int, input().split())

    n_list = [i for i in range(n)]
    n_comb = list(combinations(n_list, k))
    print(len(n_comb))