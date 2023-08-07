def solution(dolls):
    is_use_item = False
    time_use_item = 0
    score = len(dolls)  # base score
    for row in range(len(dolls)):
        second, get_item = dolls[row][0], dolls[row][1]

        is_use_item = (second - time_use_item) < 30

        if is_use_item: score += 50

        if get_item == 1:
            score += (row) * 10
            is_use_item = True
            time_use_item = second

        return score
