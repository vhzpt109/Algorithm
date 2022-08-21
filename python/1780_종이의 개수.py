def split_paper(paper, x, y, n):
    number = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if number != paper[i][j]:
                for ii in range(3):
                    for jj in range(3):
                        split_paper(paper, x + (n // 3) * ii, y + (n // 3) * jj, n // 3)
                return
    if number == -1:
        global minus_one_paper_count
        minus_one_paper_count += 1
    elif number == 0:
        global zero_paper_count
        zero_paper_count += 1
    elif number == 1:
        global plus_one_paper_count
        plus_one_paper_count += 1


if __name__ == "__main__":
    n = int(input())
    paper = []
    for i in range(n):
        paper.append(list(map(int, input().split())))

    minus_one_paper_count = 0
    zero_paper_count = 0
    plus_one_paper_count = 0

    split_paper(paper, 0, 0, n)

    print(minus_one_paper_count)
    print(zero_paper_count)
    print(plus_one_paper_count)