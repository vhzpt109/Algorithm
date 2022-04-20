if __name__ == "__main__":
    n, k = map(int, input().split())

    kind_of_coin = []
    for _ in range(n):
        kind_of_coin.append(int(input()))
    kind_of_coin.sort(reverse=True)

    coin_cnt = 0
    for coin in kind_of_coin:
        if k >= coin:
            coin_cnt += k // coin
            k = k % coin
    print(coin_cnt)