import sys
from collections import deque

input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input())

    queue = deque([])
    while True:
        command = int(input())
        if command == -1:
            if queue:
                print(*queue)
            else:
                print("empty")
            exit(0)
        elif command == 0:
            queue.popleft()
        else:
            if len(queue) == n:
                pass
            else:
                queue.append(command)