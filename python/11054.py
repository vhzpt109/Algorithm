if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))

    max_value_idx_list = [x for x, y in enumerate(A) if y == max(A)]
    longest_list = []
    for max_value_idx in max_value_idx_list:
        dp = [1] * n
        for i in range(max_value_idx + 1):
            for j in range(i):
                if A[i] > A[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        for i in range(max_value_idx, n):
            for j in range(i):
                if A[i] < A[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        longest_list.append(max(dp))
    print(max(longest_list))