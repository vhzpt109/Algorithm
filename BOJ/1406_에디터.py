import sys


input = sys.stdin.readline
if __name__ == "__main__":
    _string1 = list(input().rstrip())
    _string2 = []

    m = int(input())
    for _ in range(m):
        operation = input().split()
        if operation[0] == 'L':
            if _string1:
                _string2.append(_string1.pop())
        elif operation[0] == 'D':
            if _string2:
                _string1.append(_string2.pop())
        elif operation[0] == 'B':
            if _string1:
                _string1.pop()
        else:
            _string1.append(operation[1])

    _string1.extend(reversed(_string2))
    print(''.join(_string1))