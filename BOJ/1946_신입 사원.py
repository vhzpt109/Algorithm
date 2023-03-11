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

        _min = applicant[0][1]
        for i in range(1, len(applicant)):
            if applicant[i][1] < _min:
                _min = applicant[i][1]
                passer += 1
        print(passer)