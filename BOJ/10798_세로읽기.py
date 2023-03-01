if __name__ == "__main__":
    letters = []
    for _ in range(5):
        letter = list(input())
        letters.append(letter)

    for x in range(15):
        for y in range(5):
            try:
                print(letters[y][x], end='')
            except:
                pass