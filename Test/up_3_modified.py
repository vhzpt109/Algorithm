def solution(dolls) -> int:
    is_use_item = False
    time_use_item = -1
    score = len(dolls)  # base score
    for row in range(len(dolls)):
        second, get_item = dolls[row][0], dolls[row][1]

        if is_use_item:
            score += 50
            is_use_item = (second - time_use_item) < 30

        if get_item == 1:
            score += (row) * 10
            is_use_item = True
            time_use_item = second

        return score
