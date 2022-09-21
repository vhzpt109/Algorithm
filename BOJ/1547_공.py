if __name__ == "__main__":
    m = int(input())
    cup_list = [1, 2, 3]
    for _ in range(m):
        x, y = map(int, input().split())
        x_index = cup_list.index(x)
        y_index = cup_list.index(y)
        cup_list[x_index] = y
        cup_list[y_index] = x
    print(cup_list[0])