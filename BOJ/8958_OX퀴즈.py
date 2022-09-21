if __name__ == "__main__":
    n = int(input())
    OX_list = []
    for _ in range(n):
        OX_list.append(str(input()))

    for i in range(n):
        score = 0
        extra_score = 0
        for j in range(len(OX_list[i])):
            if OX_list[i][j] == "O":
                score = score + 1 + extra_score
                extra_score += 1
            else:
                extra_score = 0
        print(score)