if __name__ == "__main__":
    piece = [1, 1, 2, 2, 2, 8]

    current_piece = list(map(int, input().split()))

    for i in range(len(piece)):
        print(piece[i] - current_piece[i], end=" ")