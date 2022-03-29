if __name__ == "__main__":
    c = int(input())
    for _ in range(c):
        scores = list(map(int, input().split()))

        average = sum(scores[1:]) / scores[0]
        count = 0

        for score in scores[1:]:
            if score > average:
                count += 1
        rate = count / scores[0] * 100
        print('%.3f%%' % rate)