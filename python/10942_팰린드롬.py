import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    n_list = list(map(int, input().split()))

    m = int(input())
    for _ in range(m):
        s, e = map(int, input().split())
        sub_string = n_list[s - 1:e]
        if sub_string == sub_string[::-1]:
            print(1)
        else:
            print(0)