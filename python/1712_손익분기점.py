if __name__ == "__main__":
    a, b, c = map(int, input().split())

    break_even_point = -1

    if b < c:
        break_even_point = int(a / abs(b - c)) + 1

    print(break_even_point)