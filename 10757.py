if __name__ == "__main__":
    # a, b = map(int, input().split()) # easy approach
    # print(a + b)

    a, b = list(map(str, input().split()))

    a = list(map(int, a))
    b = list(map(int, b))

    if len(a) < len(b):
        temp = a
        a = b
        b = temp
    elif len(a) == len(b):
        if a[0] < b[0]:
            temp = a
            a = b
            b = temp

    result = []
    diff = len(a) - len(b)
    for i in reversed(range(len(b))):
        sum = a[i + diff] + b[i]
        if sum >= 10:
            if i == 0 and diff > 0:
                a[i + diff] = sum - 10
                a[i + diff - 1] += 1
            elif i == 0 and diff == 0:
                a[i + diff] = sum
            else:
                a[i + diff] = sum - 10
                a[i + diff - 1] += 1
        else:
            a[i + diff] = sum

    # for i in reversed(range(diff)):
    #     if a[i] >= 10:
    #         if i == 0:
    #             result.append(a[i] - 10)
    #             result.append(1)
    #         else:
    #             result.append(a[i] - 10)
    #             a[i - 1] += 1
    #     else:
    #         result.append(a[i])

    for i in a:
        print(i, end="")