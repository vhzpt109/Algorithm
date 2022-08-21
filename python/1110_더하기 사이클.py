if __name__ == "__main__":
    n = int(input())
    cycle_len = 0
    if n < 10:
        n = n * 10
    n_temp = n
    while True:
        cycle_len = cycle_len + 1
        tens = n_temp // 10
        units = n_temp % 10
        n_temp = units * 10 + (tens + units) % 10
        if n_temp == n:
            break
    print(cycle_len)
