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
        use_flag = False
        for j in range(n):
            for l in range(i, k):
                if schedule[l] == multitap[j]:
                    if last_use_index < l:
                        last_use_index = l
                        last_use_item = multitap[j]
                if last_use_index == -1:
                    multitap.remove(multitap[j])
                    multitap.append(schedule[i])
                    count += 1
                    use_flag = True
                    break
            if use_flag:
                break

        if not use_flag:
            multitap.remove(schedule[last_use_index])
            multitap.append(schedule[i])
            count += 1
    print(count)