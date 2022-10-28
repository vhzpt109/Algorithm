if __name__ == "__main__":
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.sort()

    print(sum(n_list[n - 1 - i] - n_list[i] for i in range(n)))