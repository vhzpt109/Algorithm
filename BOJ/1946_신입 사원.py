import sys

input = sys.stdin.readline
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        applicant = []
        passer = 1
        for _ in range(n):
            applicant.append(list(map(int, input().split())))
        applicant.sort()

        for i in range(len(applicant) - 1):
            if applicant[i][1] > applicant[i + 1][1]:
                passer += 1
        print(passer)