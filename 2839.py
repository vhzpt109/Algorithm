import sys

if __name__ == "__main__":
    n = int(input())

    max_n_5kg_bag = n // 5
    max_n_3kg_bag = n // 3

    min_kg = sys.maxsize
    min_bag = -1
    for i in reversed(range(max_n_5kg_bag + 1)):
        for j in reversed(range(max_n_3kg_bag + 1)):
            if i == 0 and j == 0:
                continue
            kg = i * 5 + j * 3
            if kg - n != 0:
                continue
            if kg < min_kg:
                min_kg = kg
                min_bag = i + j
    print(min_bag)