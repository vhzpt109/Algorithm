import math

if __name__ == "__main__":
    n, m = map(int, input().split())

    print(math.gcd(n, m))
    print(math.lcm(n, m))