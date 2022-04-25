import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    n_list = []
    for _ in range(n):
        n_list.append(int(sys.stdin.readline()))
    n_list.reverse()

    i = 0
    stack = []
    stack_history = []
    while i < n:
        if stack[-1] == n_list[-1]:
            stack.pop()
            n_list.pop()
            stack_history.append("-")
        else:
            i += 1
            stack.append(i)
            stack_history.append("+")

        if i > n:
            break

    print(stack_history)

    # if stack_history.count("+") == stack_history.count("-"):
    #     for stack in stack_history:
    #         print(stack)
    # else:
    #     print("NO")