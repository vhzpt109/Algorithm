if __name__ == "__main__":
    n, k = map(int, input().split())
    schedule = list(map(int, input().split()))

    count = 0

    multitap = []
    for i in range(k):
        if schedule[i] in multitap:
            continue

        if len(multitap) < n:
            multitap.append(schedule[i])
            continue

        last_use_index = 0
        temp = 0
        for item in multitap:
            if item not in schedule[i:]:
                temp = item
                break
            elif schedule[i:].index(item) > last_use_index:
                last_use_index = schedule[i:].index(item)
                temp = item
        multitap[multitap.index(temp)] = schedule[i]
        count += 1

    print(count)