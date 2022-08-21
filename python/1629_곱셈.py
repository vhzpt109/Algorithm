def DivideConquer(n, exponent):
    global C
    if exponent == 1:
        return n % C

    temp = DivideConquer(n, exponent // 2)

    if exponent % 2 == 0:
        return temp * temp % C
    else:
        return temp * temp * n % C


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    print(DivideConquer(A, B))