from collections import Counter

n = 0
house = 2


def dfs(house_map, x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if house_map[x][y] == 1:
        house_map[x][y] = house
        dfs(house_map, x - 1, y)
        dfs(house_map, x, y - 1)
        dfs(house_map, x + 1, y)
        dfs(house_map, x, y + 1)
        return True
    else:
        return False


if __name__ == "__main__":
    n = int(input())
    house_map = []
    for _ in range(n):
        house_map.append(list(map(int, input())))

    for y in range(n):
        for x in range(n):
            if dfs(house_map, x, y):
                house += 1
    print(house - 2)

    house_count = []
    for i in range(2, house):
        house_count.append(sum([row.count(i) for row in house_map]))
    house_count.sort()

    for count in house_count:
        print(count)