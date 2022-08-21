import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    site_dict = {}
    for _ in range(n):
        site, password = map(str, input().split())
        site_dict[site] = password

    for _ in range(m):
        print(site_dict[input().rstrip()])