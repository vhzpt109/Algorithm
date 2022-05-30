if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        p = list(input())
        p_tuning = p[0]
        count = 0
        for func in p:
            if func == p_tuning[-1]:
                count += 1
            else:
                p_tuning += str(count) + func
                count = 1
        p_tuning += str(count)
        p_tuning = list(p_tuning)

        n = int(input())
        n_list = list(input()[1:-1].split(','))

        error_check = False
        for i in range(0, len(p_tuning), 2):
            if p_tuning[i] == 'R':
                if int(p_tuning[i + 1]) % 2 != 0:
                    n_list.reverse()
            elif p_tuning[i] == 'D':
                for d_n in range(int(p_tuning[i + 1])):
                    if n > 1:
                        n_list.pop(0)
                        n -= 1
                    else:
                        error_check = True
                        break
            if error_check:
                break

        if not error_check:
            print("[", end="")
            for n in n_list[:-1]:
                print(n + ",", end="")
            print(n_list[-1] + "]")
        else:
            print("error")