if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))

    dp_inc = [1] * n
    for i in range(n):
        for j in range(i):
            if A[i] > A[j]:
                dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)

    A.reverse()
    dp_dec = [1] * n
    for i in range(n):
        for j in range(i):
            if A[i] > A[j]:
                dp_dec[i] = max(dp_dec[i], dp_dec[j] + 1)
    dp_dec.reverse()

    dp_sum = [dp_inc[i] + dp_dec[i] for i in range(n)]
    print(max(dp_sum) - 1)