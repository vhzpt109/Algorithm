import math


def solution(resistors):
    min_amp = 10001
    sum_ohm = 0
    for resistor in resistors:
        ohm, w = resistor[0], resistor[1]
        sum_ohm += ohm
        amp = math.sqrt(w / ohm)
        min_amp = min(min_amp, amp)

    answer = int(min_amp**2 * sum_ohm)

    return answer