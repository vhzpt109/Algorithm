import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().rstrip())
    n_list = list(map(int, input().rstrip().split()))

    m = int(input().rstrip())
    for _ in range(m):
        s, e = map(int, input(),rstrip().split())
        sub_string = n_list[s - 1:e]
        if sub_string == sub_string[::-1]:
            print(1)
        else:
            print(0)