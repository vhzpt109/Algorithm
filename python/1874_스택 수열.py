import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    n_list = []
    for _ in range(n):
        n_list.append(int(sys.stdin.readline()))
    n_list.reverse()

    i = 1
    stack = []
    stack_history = []
    not_sequence = False
    while True:
        if len(stack) > 0:
            if stack[-1] == n_list[-1]:
                stack.pop()
                n_list.pop()
                stack_history.append("-")
            elif stack[-1] > n_list[-1]:
                not_sequence = True
                break
            else:
                stack.append(i)
                stack_history.append("+")
                i += 1
        elif i < (n + 1):
            stack.append(i)
            stack_history.append("+")
            i += 1
        else:
            break

    if not_sequence:
        print("NO")
    else:
        for history in stack_history:
            print(history)