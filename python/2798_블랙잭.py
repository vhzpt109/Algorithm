from itertools import combinations

if __name__ == "__main__":
    m, n = map(int, input().split())

    list_m = list(map(int, input().split()))

    max = 0
    for cards in combinations(list_m, 3):
        card_sum = sum(cards)
        if max < card_sum <= n:
            max = card_sum
    print(max)