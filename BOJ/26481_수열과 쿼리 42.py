if __name__ == "__main__":
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(q):
        i, j = map(int, input().split())
        A_sub = A[i:j + 1]

        dp = [1] * len(A_sub)
        for a in range(len(A_sub)):
            for b in range(a):
                if A[a] > A[b]:
                    dp[a] = max(dp[a], dp[b] + 1)
        print(max(dp))