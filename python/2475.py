if __name__ == "__main__":
    serial_number = list(map(int, input().split()))

    pow_sum = 0
    for number in serial_number:
        pow_sum += number**2
    print(pow_sum % 10)