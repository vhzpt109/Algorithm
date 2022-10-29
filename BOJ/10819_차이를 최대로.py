def backtracking(x):
    if x == n:
        result_list.append(sum(abs(m[temp[i + 1]] - m[temp[i]]) for i in range(n - 1)))
        return

    for i in range(n):
        if i not in temp:
            temp.append(i)
            backtracking(x + 1)
            temp.pop()


if __name__ == "__main__":
    n = int(input())
    m = list(map(int, input().split()))
    result_list = []
    temp = []
    backtracking(0)

    print(max(result_list))