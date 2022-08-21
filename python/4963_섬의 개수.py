import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

label = 0

def dfs(island_map, x, y):
    if x <= -1 or x >= w or y <= -1 or y >= h:
        return False

    if island_map[y][x] == 1:
        island_map[y][x] = label
        dfs(island_map, x - 1, y - 1)
        dfs(island_map, x - 1, y)
        dfs(island_map, x + 1, y - 1)
        dfs(island_map, x + 1, y)
        dfs(island_map, x + 1, y + 1)
        dfs(island_map, x, y + 1)
        dfs(island_map, x - 1, y + 1)
        dfs(island_map, x, y - 1)
        return True
    else:
        return False

if __name__ == "__main__":
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break

        label = 100
        island_map = []
        for _ in range(h):
            island_map.append(list(map(int, input().split())))

        for y in range(h):
            for x in range(w):
                if dfs(island_map, x, y):
                    label += 1
        print(label - 100)