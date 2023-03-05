if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())

        sticker = [list(map(int, input().split())) for _ in range(2)]
        sticker[0].insert(0, 0)
        sticker[1].insert(0, 0)

        dp1 = [0 for _ in range(n + 1)]
        dp2 = [0 for _ in range(n + 1)]
        dp1[1] = sticker[0][1]
        dp2[1] = sticker[1][1]
        for i in range(2, n + 1):
            dp1[i] = max(dp2[i - 1], dp1[i - 2], dp2[i - 2]) + sticker[0][i]
            dp2[i] = max(dp1[i - 1], dp2[i - 2], dp1[i - 2]) + sticker[1][i]

        print(max(dp1[n], dp2[n]))