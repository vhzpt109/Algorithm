if __name__ == "__main__":
    n = int(input())
    divisor_list = list(map(int, input().split()))

    print(min(divisor_list) * max(divisor_list))