from collections import deque

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        importance_queue = deque(list(map(int, input().split())))
        max_importance = max(importance_queue)
        target_importance = importance_queue[m]
        count = 0

        while True:
            popleft = importance_queue.popleft()
            if popleft == max_importance:
                if popleft == target_importance:
                    print(count)
                    break
                else:
                    count += 1
                max_importance = max(importance_queue)
            else:
                importance_queue.append(popleft)
                count += 1