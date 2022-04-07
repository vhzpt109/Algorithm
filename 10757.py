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

    result = []
    for i in reversed(range(len(a))):
        sum = a[i] + b[i]
        if sum >= 10:
            sum -= 10
            if i > 0:
                result.append(sum)
                a[i - 1] += 1
            else:
                result.append(sum)
                result.append(1)
        else:
            result.append(sum)

    for i in reversed(range(len(a) - len(b))):
        if a[i] >= 10:
            a[i - 1] += 1
        result.append(a[i])

    for i in result[::-1]:
        print(i, end="")