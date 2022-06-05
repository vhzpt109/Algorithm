import sys
from collections import Counter

if __name__ == "__main__":
    n, m, b = map(int, sys.stdin.readline().split())

    block = []
    for _ in range(n):
        block += (list(map(int, sys.stdin.readline().split())))
    block_counter = Counter(block)

    max_block = max(block)
    min_block = min(block)

    min_cost = sys.maxsize
    min_cost_height = 0
    for height in range(min_block, max_block + 1):
        cost = 0
        inventory = b
        for h, c in block_counter.items():
            if h > height:
                cost += (h - height) * 2 * c
                inventory += (h - height) * c
            else:
                cost += (height - h) * c
                inventory -= (height - h) * c

        if inventory < 0:
            continue

        if min_cost >= cost:
            min_cost = cost
            min_cost_height = max(height, min_cost_height)

    print(min_cost, min_cost_height)