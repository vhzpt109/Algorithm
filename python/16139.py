import sys

if __name__ == "__main__":
    s = sys.stdin.readline()
    q = int(sys.stdin.readline())
    for _ in range(q):
        a, l, r = map(str, sys.stdin.readline().split())
        l, r = int(l), int(r)

        s_lr = sorted(s[l:r + 1])
        s_lr = ''.join(s_lr)

        start = s_lr.find(a)
        if start == -1:
            sys.stdout.write(str(0) + "\n")
            continue
        end = s_lr.rfind(a)

        sys.stdout.write(str(end - start + 1) + "\n")