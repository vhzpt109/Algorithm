if __name__ == "__main__":
    factorial = [0] * 501
    factorial[0] = 1
    factorial[1] = 1
    for i in range(2, len(factorial)):
        factorial[i] = factorial[i - 1] * i

    n = int(input())
    cnt = 0
    for s in reversed(str(factorial[n])):
        if s == '0':
            cnt += 1
        else:
            break
    print(cnt)