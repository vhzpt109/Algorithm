if __name__ == "__main__":
    n = int(input())
    h_list = list(map(int, input().split()))
    a_list = list(map(int, input().split()))

    temp = [[h_list[x], a_list[x]] for x in range(n)] # 반복문을 통해
    temp = sorted(temp, key=lambda x: x[1])

    result = [temp[i][0] + (temp[i][1] * i) for i in range(n)]
    print(sum(result))