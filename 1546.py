if __name__ == "__main__":
    n = int(input())
    score = list(map(int, input().split()))
    new_score = 0

    if len(score) != n:
        exit()

    score.sort()

    for i in range(len(score)):
        new_score += (score[i] / score[-1] * 100)

    print(new_score / n)