move = []


def hanoi(num, starting, destination, other):
    if num == 0:
        return
    hanoi(num - 1, starting, other, destination)
    move.append([starting + 1, destination + 1])
    hanoi(num - 1, other, destination, starting)


if __name__ == "__main__":
    n = int(input())

    hanoi(n, 0, 2, 1)

    print(len(move))

    for i in move:
        print(i[0], i[1])