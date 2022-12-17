import sys

input = sys.stdin.readline
if __name__ == "__main__":
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(q):
        l, r = map(int, input().split())
        A_sub = A[l - 1:r]

        dp = [1] * len(A_sub)
        for k in range(len(A_sub)):
            for i in range(k):
                if A_sub[i] < A_sub[k]:
                    dp[k] = max(dp[k], dp[i] + 1)
        print(max(dp))