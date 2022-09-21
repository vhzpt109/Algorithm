import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    rope_weight_list = []
    for _ in range(n):
        rope_weight_list.append(int(input()))
    rope_weight_list.sort(reverse=True)

    max_rope_weight = 0
    for i in range(0, n):
        rope_weight = rope_weight_list[i] * (i + 1)
        max_rope_weight = max(max_rope_weight, rope_weight)
    print(max_rope_weight)