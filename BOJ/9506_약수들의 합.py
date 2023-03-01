if __name__ == "__main__":
    n = int(input())
    while n != -1:
        divisor_list = []
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                divisor_list.append(i)
        if sum(divisor_list) == n:
            print(n, "= ", end='')
            for i in range(len(divisor_list) - 1):
                print(divisor_list[i], "+ ", end='')
            print(divisor_list[-1])
        else:
            print(n, "is NOT perfect.")

        n = int(input())