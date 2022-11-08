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

        for j in range(k):
            # Search Page Replacement Algorithm..
