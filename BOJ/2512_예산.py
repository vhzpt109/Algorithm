def binary_search(budget_list, total_budget, start, end):
    while start <= end:
        mid = (start + end) // 2
        sum_budget = 0
        for budget in budget_list:
            sum_budget += (budget - mid)

        if sum_budget > total_budget:
            end = mid - 1
        else:
            start = mid + 1
    return end


if __name__ == "__main__":
    n = int(input())
    budget_list = list(map(int, input().split()))
    total_budget = int(input())
    print(binary_search(budget_list, total_budget, 0, max(budget_list)))

