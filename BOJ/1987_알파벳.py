from string import ascii_uppercase
import copy


def dfs(board, alphabet_count, visited, x, y, count):
    visited[y][x] = True
    alphabet_count[board[y][x]] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    max_count = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if xx < 0 or xx >= c or yy < 0 or yy >= r:
            continue
        if alphabet_count[board[yy][xx]] == 0:
            continue
        if visited[yy][xx]:
            continue

        clone_alphabet_count = copy.deepcopy(alphabet_count)
        max_count = max(dfs(board[:], clone_alphabet_count, visited[:], xx, yy, count + 1), count)

    return max_count


if __name__ == "__main__":
    r, c = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(r)]
    visited = [[False for _ in range(c)] for _ in range(r)]

    alphabet_count = {}
    for alphabet in list(ascii_uppercase):
        alphabet_count[alphabet] = 1

    print(dfs(board[:], copy.deepcopy(alphabet_count), visited[:], 0, 0, 1))
