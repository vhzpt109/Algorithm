import sys
input = sys.stdin.readline


def dfs(board, alphabet_count, visited, x, y, count):
    visited[y][x] = True
    alphabet_count[ord(board[y][x]) - 65] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    max_count = count
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if xx < 0 or xx >= c or yy < 0 or yy >= r:
            continue
        if alphabet_count[ord(board[yy][xx]) - 65] == 0:
            continue
        if visited[yy][xx]:
            continue

        max_count = max(dfs(board, alphabet_count, visited, xx, yy, count + 1), max_count)
        visited[yy][xx] = False
        alphabet_count[ord(board[yy][xx]) - 65] = 1

    return max_count


if __name__ == "__main__":
    r, c = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(r)]
    visited = [[False for _ in range(c)] for _ in range(r)]

    alphabet_count = [1 for _ in range(26)]

    print(dfs(board, alphabet_count, visited, 0, 0, 1))