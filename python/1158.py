from collections import deque

if __name__ == "__main__":
    n, k = map(int, input().split())
    queue = deque([i for i in range(1, n + 1)])
    result_list = []

    i = 0
    while len(queue) != 0:
        i += 1
        if i % k == 0:
            result_list.append(queue.popleft())
        else:
            queue.append(queue.popleft())

    print("<", end="")
    for result in result_list[:-1]:
        print(result, end=", ")
    print(str(result_list[-1]) + ">")