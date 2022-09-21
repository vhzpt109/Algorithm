if __name__ == "__main__":
    n_stairs = int(input())
    stairs_list = [-1]
    for _ in range(n_stairs):
        stairs_list.append(int(input()))

    dp = [-1] * (n_stairs + 1)
    near_count = 0

    if n_stairs < 4:
        if n_stairs == 1:
            print(stairs_list[1])
        elif n_stairs == 2:
            print(stairs_list[1] + stairs_list[2])
        elif n_stairs == 3:
            print(max(stairs_list[1] + stairs_list[3], stairs_list[2] + stairs_list[3]))
        exit()

    dp[1] = stairs_list[1]
    dp[2] = stairs_list[1] + stairs_list[2]
    dp[3] = max(stairs_list[1] + stairs_list[3], stairs_list[2] + stairs_list[3])

    for i in range(4, n_stairs + 1):
        dp[i] = max(dp[i - 2] + stairs_list[i], dp[i - 3] + stairs_list[i - 1] + stairs_list[i])

    print(dp[n_stairs])