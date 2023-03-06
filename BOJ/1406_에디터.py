if __name__ == "__main__":
    _string = list(input().rstrip())

    cursor = len(_string)
    m = int(input())
    for _ in range(m):
        operation = input().split()
        if operation[0] == 'L':
            if cursor > 0:
                cursor -= 1
        elif operation[0] == 'D':
            if cursor < len(_string):
                cursor += 1
        elif operation[0] == 'B':
            if cursor > 0:
                _string.remove(_string[cursor - 1])
                cursor -= 1
        else:
            _string.insert(cursor, operation[1])
            cursor += 1

    print(''.join(_string))