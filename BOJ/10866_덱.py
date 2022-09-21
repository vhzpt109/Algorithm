import sys
from collections import deque

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    queue = deque([])

    for _ in range(n):
        command = sys.stdin.readline()
        if "push_front" in command:
            queue.appendleft(command.split()[1])
        elif "push_back" in command:
            queue.append(command.split()[1])
        elif "pop_front" in command:
            if len(queue) > 0:
                print(queue.popleft())
            else:
                print(-1)
        elif "pop_back" in command:
            if len(queue) > 0:
                print(queue.pop())
            else:
                print(-1)
        elif "size" in command:
            print(len(queue))
        elif "empty" in command:
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif "front" in command:
            if len(queue) > 0:
                print(queue[0])
            else:
                print(-1)
        elif "back" in command:
            if len(queue) > 0:
                print(queue[-1])
            else:
                print(-1)