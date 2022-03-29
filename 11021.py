if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        print("Case #" + str(i + 1) + ":", a + b)