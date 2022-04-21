import sys
from collections import Counter

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    list_n = []
    for _ in range(n):
        list_n.append(int(sys.stdin.readline()))
    list_n.sort()

    average = round(sum(list_n) / len(list_n))
    median = list_n[int(len(list_n) / 2)]
    most_common = Counter(list_n).most_common(2)
    if len(most_common) > 1:
        mode = most_common[0][0] if most_common[0][1] != most_common[1][1] else most_common[1][0]
    else:
        mode = most_common[0][0]
    range = list_n[-1] - list_n[0]

    print(average)
    print(median)
    print(mode)
    print(range)