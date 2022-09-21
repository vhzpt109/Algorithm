if __name__ == "__main__":
    n = int(input())

    t_list = [0]
    p_list = [0]
    for _ in range(n):
        t, p = map(int, input().split())
        t_list.append(t)
        p_list.append(p)

    dp = [0] * (n + 1)
    dp[1] = p_list[1]

    for i in range(2, n + 1):
        if n + 1 - i < t_list[i]:
            continue
        for j in range(1, i):
            if i - j >= t_list[j]:
                dp[i] = max(p_list[i] + dp[j], dp[i])
    print(max(dp))