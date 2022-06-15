def compression(gray_image, x, y, n):
    pixel = gray_image[y][x]
    for i in range(y, y + n):
        for j in range(x, x + n):
            if pixel != gray_image[i][j]:
                print("(", end="")
                compression(gray_image, x, y, n // 2)
                compression(gray_image, x + n // 2, y, n // 2)
                compression(gray_image, x, y + n // 2, n // 2)
                compression(gray_image, x + n // 2, y + n // 2, n // 2)
                print(")", end="")
                return

    if pixel == "0":
        print("0", end="")
    else:
        print("1", end="")


if __name__ == "__main__":
    n = int(input())
    gray_image = []
    for i in range(n):
        gray_image.append(list(input()))

    compression(gray_image, 0, 0, n)