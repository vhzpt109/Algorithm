import sys

input = sys.stdin.readline
if __name__ == "__main__":
    s = input().rstrip()
    p = input().rstrip()

    p_hash = hash(p)
    for i in range(len(s) - len(p) + 1):
        sub_s_hash = hash(s[i:i + len(p)])
        if sub_s_hash == p_hash:
            print(1)
            exit(0)
    print(0)