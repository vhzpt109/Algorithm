if __name__ == "__main__":
    x = int(input())
    n = int(input())

    amount_sum = 0
    for _ in range(n):
        a, b = map(int, input().split())
        amount_sum += a * b

    if x == amount_sum:
        print("Yes")
    else:
        print("No")