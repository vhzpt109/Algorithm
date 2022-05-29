if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        importance_queue = list(map(int, input().split()))
        importance_queue = [(i, idx) for idx, i in enumerate(importance_queue)]

        max_importance = max(importance_queue, key=lambda x: x[0])[0]
        count = 0

        while True:
            popleft = importance_queue.pop(0)
            if popleft[0] == max_importance:
                count += 1
                if popleft[1] == m:
                    print(count)
                    break
                else:
                    max_importance = max(importance_queue, key=lambda x: x[0])[0]
            else:
                importance_queue.append(popleft)