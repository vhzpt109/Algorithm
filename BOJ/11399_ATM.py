if __name__ == "__main__":
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()

    cost_sum = 0
    for i in range(n):
        for j in range(i + 1):
            cost_sum += s[j]
    print(cost_sum)