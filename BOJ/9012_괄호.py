import sys

if __name__ == "__main__":
    t = int(sys.stdin.readline())

    for _ in range(t):
        ps = []
        x = sys.stdin.readline()
        for s in x:
            if s == "(":
                ps.append(s)
            elif s == ")":
                if len(ps) == 0:
                    print("NO")
                    break
                else:
                    ps.pop()
        else:
            if len(ps) == 0:
                print("YES")
            else:
                print("NO")