import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())

    n_list = list()
    n_dict = {}
    for i in range(n):
        name = sys.stdin.readline().rstrip()
        n_list.append(name)
        n_dict[name] = i + 1

    for _ in range(m):
        func = sys.stdin.readline().rstrip()
        if func.isdigit():
            print(n_list[int(func) - 1])
        else:
            print(n_dict[func])