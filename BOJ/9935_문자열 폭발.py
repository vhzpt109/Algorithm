if __name__ == "__main__":
    _string = input().rstrip()
    explosion_string = input().rstrip()

    stack = []

    for i in range(len(_string)):
        stack.append(_string[i])
        if ''.join(stack[-len(explosion_string):]) == explosion_string:
            for _ in range(len(explosion_string)):
                stack.pop()


    if stack:
        print(''.join(stack))

    else:
        print("FRULA")