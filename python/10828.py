import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    stack = []

    for _ in range(n):
        command = sys.stdin.readline()
        if "push" in command:
            stack.append(command.split()[1])
        elif "pop" in command:
            if len(stack) > 0:
                print(stack[-1])
                stack.pop()
            else:
                print(-1)
        elif "size" in command:
            print(len(stack))
        elif "empty" in command:
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif "top" in command:
            if len(stack) > 0:
                print(stack[-1])
            else:
                print(-1)