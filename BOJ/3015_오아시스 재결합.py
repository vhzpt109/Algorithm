import sys

input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input())

    facetoface = 0
    stack = [int(input())]
    for _ in range(n - 1):
        now = int(input())

        while now < stack[-1] and stack:
            stack.pop()
            facetoface += 1

        if now > stack[-1] and stack:
            stack.append(now)
            facetoface += 1

    print(facetoface)