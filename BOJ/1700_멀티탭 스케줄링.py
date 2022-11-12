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

        last_use_index, last_use_item = -1, -1
        stop_search_flag = False
        for j in range(n):
            for l in range(i, k):
                use_flag = False
                if schedule[l] == multitap[j]:
                    use_flag = True
                    if last_use_index < l:
                        last_use_index = l
                        last_use_item = multitap[j]

                if not use_flag:
                    multitap.remove(multitap[j])
                    multitap.append(schedule[i])
                    count += 1
                    stop_search_flag = True
                    break

            if stop_search_flag:
                break

        if stop_search_flag:
            multitap.remove(schedule[last_use_index])
            multitap.append(schedule[i])
            count += 1
    print(count)