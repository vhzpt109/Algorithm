import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(cabbage_map, x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False

    if cabbage_map[y][x] == 1:
        cabbage_map[y][x] = 0
        dfs(cabbage_map, x - 1, y)
        dfs(cabbage_map, x, y - 1)
        dfs(cabbage_map, x + 1, y)
        dfs(cabbage_map, x, y + 1)
        return True
    else:
        return False


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        cabbage_field = [[0] * m for _ in range(n)]
        earthworm_count = 0
        for _ in range(k):
            x, y = map(int, input().split())
            cabbage_field[y][x] = 1
        for y in range(n):
            for x in range(m):
                if dfs(cabbage_field, x, y):
                    earthworm_count += 1
        print(earthworm_count)