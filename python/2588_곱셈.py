if __name__ == "__main__":
    a, b = map(int, input())
    print(a * (b % 10))
    print(a * ((b % 100) // 10))
    print(a * (b // 100))
    print(a * b)
