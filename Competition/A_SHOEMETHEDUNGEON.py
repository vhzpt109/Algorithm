if __name__ == "__main__":
    n, k = map(int, input().split())
    A_list = list(map, input().split())
    P_list = list(map, input().split())

    if k < min(A_list):
        print(0)
        exit()