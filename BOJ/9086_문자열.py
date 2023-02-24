if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        testCase = input().rstrip()
        print(testCase[0], end='')
        print(testCase[-1])