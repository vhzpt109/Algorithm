if __name__ == "__main__":
    n_wines = int(input())
    wine_list = [-1]
    for _ in range(n_wines):
        wine_list.append(int(input()))

    dp = [-1] * (n_wines + 1)

    if n_wines < 4:
        if n_wines == 1:
            print(wine_list[1])
        elif n_wines == 2:
            print(wine_list[1] + wine_list[2])
        elif n_wines == 3:
            print(max(wine_list[1] + wine_list[2], wine_list[1] + wine_list[3], wine_list[2] + wine_list[3]))
        exit()

    dp[1] = wine_list[1]
    dp[2] = wine_list[1] + wine_list[2]
    dp[3] = max(wine_list[1] + wine_list[2], wine_list[1] + wine_list[3], wine_list[2] + wine_list[3])

    for i in range(4, n_wines + 1):
        dp[i] = max(dp[i - 2] + wine_list[i], dp[i - 3] + wine_list[i - 1] + wine_list[i], dp[i - 1])

    print(max(dp))