if __name__ == "__main__":
    n_list = list(input())

    n_list.sort(reverse=True)

    for n in n_list:
        print(n, end="")