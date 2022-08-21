if __name__ == "__main__":
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    sum_list = [0, A[0]]

    for i in range(1, n):
        sum_list.append(sum_list[i] + A[i])

    result = [0] * 1000
    for i in range(1, n + 1):
        result[sum_list[i] % m] += 1

    count = result[0]
    for i in range(len(result)):
        if result[i] < 1:
            continue
        else:
            count += result[i] * (result[i] - 1) / 2.
    print(int(count))