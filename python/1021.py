from collections import deque

if __name__ == "__main__":
    n, m = map(int, input().split())
    target_list = list(map(int, input().split()))

    queue = deque([i for i in range(1, n + 1)])

    count = 0
    while target_list:
        if queue[0] == target_list[0]:
            queue.popleft()
            target_list.remove(target_list[0])
        elif queue.index(target_list[0]) > len(queue) / 2:
            queue.rotate(1)
            count += 1
        else:
            queue.rotate(-1)
            count += 1
    print(count)