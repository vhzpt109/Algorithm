import sys

input = sys.stdin.readline
if __name__ == "__main__":
    s = input().rstrip()
    n = int(input())

    count = 0
    for _ in range(n):
        find_s = input().rstrip()
        find_s += find_s
        if find_s.find(s) != -1:
            count += 1
    print(count)