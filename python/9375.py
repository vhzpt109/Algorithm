from collections import Counter

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        clothes_type = []
        n = int(input())
        for _ in range(n):
            _, type = input().split()
            clothes_type.append(type)
        clothes_type_cnt = Counter(clothes_type)

        cases = 1
        for type in clothes_type_cnt:
            cases *= clothes_type_cnt[type] + 1
        cases -= 1
        print(cases)