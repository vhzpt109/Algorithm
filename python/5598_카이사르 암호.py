if __name__ == "__main__":
    s = list(input())

    for char in s:
        caesar = chr(ord(char) - 3) if ord(char) >= 68 else chr(ord(char) + 23)
        print(caesar, end="")