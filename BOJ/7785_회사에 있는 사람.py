import sys


input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input())

    log = {}
    for _ in range(n):
        name, status = map(str, input().split())
        if status == "enter":
            log[name] = status
        else:
            log.pop(name)

    log = sorted(log.keys(), reverse=True)

    for l in log:
        print(l)