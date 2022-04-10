if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        k = int(input())
        n = int(input())

        apart = [x for x in range(1, n+1)]

        for i in range(k):
            for j in range(1, n):
                apart[j] += apart[j-1]
        print(apart[-1])