if __name__ == "__main__":
    n = int(input())
    A_list = list(map(int, input().split()))
    dp = [0]

    for A in A_list:
        if dp[-1] < A:
            dp.append(A)
        else:
            left = 0
            right = len(dp)

            while left < right:
                mid = (left + right) // 2

                if dp[mid] < A:
                    left = mid + 1
                else:
                    right = mid
            dp[right] = A
    print(len(dp) - 1)