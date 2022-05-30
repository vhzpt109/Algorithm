from collections import deque

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        p = list(input())

        n = int(input())
        n_list = deque(list(input()[1:-1].split(',')))

        error_check = False
        reverse_flag = False
        for func in p:
            if func == 'R':
                reverse_flag = not reverse_flag
            elif func == 'D':
                if n > 0:
                    n -= 1
                    if not reverse_flag:
                        n_list.popleft()
                    else:
                        n_list.pop()
                else:
                    error_check = True

        if not error_check:
            print("[", end="")
            result_n_list = list(n_list)
            if len(result_n_list) > 0:
                if reverse_flag:
                    result_n_list.reverse()
                for n in result_n_list[:-1]:
                    print(n + ",", end="")
                print(result_n_list[-1] + "]")
            else:
                print("]")
        else:
            print("error")