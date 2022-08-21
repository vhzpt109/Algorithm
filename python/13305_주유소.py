if __name__ == "__main__":
    n = int(input())
    road_length_list = list(map(int, input().split()))
    cost_city_list = list(map(int, input().split()))

    min_cost = cost_city_list[0]
    least_cost = 0

    for i in range(n - 1):
        if min_cost > cost_city_list[i]:
            min_cost = cost_city_list[i]
        least_cost += min_cost * road_length_list[i]
    print(least_cost)