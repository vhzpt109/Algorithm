if __name__ == "__main__":
    n, x = map(int, input().split())
    sequence = list(map(int, input().split()))
    for i in range(n):
        if sequence[i] < x:
            print(sequence[i], end=" ")