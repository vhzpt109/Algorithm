import sys

input = sys.stdin.readline

if __name__ == "__main__":
    s = input().rstrip()
    q = int(input())

    alphabet_prefix_sum = [[0] * 26]
    alphabet_prefix_sum[0][ord(s[0]) - 97] = 1

    for i in range(1, len(s)):
        alphabet_prefix_sum.append(alphabet_prefix_sum[-1][:])
        alphabet_prefix_sum[i][ord(s[i]) - 97] += 1

    for _ in range(q):
        a, l, r = map(str, input().rstrip().split())
        l, r = int(l), int(r)
        if l == 0:
            print(alphabet_prefix_sum[r][ord(a) - 97])
        else:
            print(alphabet_prefix_sum[r][ord(a) - 97] - alphabet_prefix_sum[l - 1][ord(a) - 97])