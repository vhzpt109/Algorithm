if __name__ == "__main__":
    t = int(input())

    time_list = [300, 60, 10]
    count_list = [0, 0, 0]
    for i in range(3):
        if t >= time_list[i]:
            count_list[i] += t // time_list[i]
            t = t % time_list[i]

    if t > 0:
        print(-1)
    else:
        print(*count_list)