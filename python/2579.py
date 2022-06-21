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
            print(max(stairs_list[2] + stairs_list[3], stairs_list[1] + stairs_list[3]))
        exit()

    dp[1] = stairs_list[1]
    dp[2] = stairs_list[1] + stairs_list[2]
    if max(stairs_list[2] + stairs_list[3], stairs_list[1] + stairs_list[3]) == stairs_list[1] + stairs_list[3]:
        dp[3] = stairs_list[1] + stairs_list[3]
    else:
        dp[3] = stairs_list[2] + stairs_list[3]
        near_count += 1

    for i in range(4, n_stairs):
        if dp[i - 1] == dp[i - 2]:
            dp[i] = dp[i - 2] + stairs_list[i]
            near_count = 0
        elif max(dp[i - 1], dp[i - 2]) == dp[i - 1] and near_count != 1:
            dp[i] = dp[i - 1] + stairs_list[i]
            near_count += 1
        else:
            dp[i] = dp[i - 2] + stairs_list[i]
            near_count = 0

    if max(dp[n_stairs - 1], dp[n_stairs - 2]) == dp[n_stairs - 1] and near_count != 1:
        dp[n_stairs] = dp[n_stairs - 1] + stairs_list[n_stairs]
    else:
        dp[n_stairs] = dp[n_stairs - 2] + stairs_list[n_stairs]

    print(dp[n_stairs])