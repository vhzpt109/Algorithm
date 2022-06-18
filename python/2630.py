def make_color_paper(color_paper, x, y, n):
    color = color_paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != color_paper[i][j]:
                make_color_paper(color_paper, x, y, n // 2)
                make_color_paper(color_paper, x + n // 2, y, n // 2)
                make_color_paper(color_paper, x, y + n // 2, n // 2)
                make_color_paper(color_paper, x + n // 2, y + n // 2, n // 2)
                return
    if color == 0:
        global white_color_paper_count
        white_color_paper_count += 1
    else:
        global blue_color_paper_count
        blue_color_paper_count += 1


if __name__ == "__main__":
    n = int(input())
    color_paper = []
    for i in range(n):
        color_paper.append(list(map(int, input().split())))

    white_color_paper_count = 0
    blue_color_paper_count = 0
    make_color_paper(color_paper, 0, 0, n)
    print(white_color_paper_count)
    print(blue_color_paper_count)