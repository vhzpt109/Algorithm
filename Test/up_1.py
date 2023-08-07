def solution(p, n):
    ampm, time = p.split(' ')
    hour, minute, second = map(int, time.split(':'))
    if ampm == "PM":
        hour += 12
    extra_hour, extra_minute, extra_second = get_extra_time(n)
    hour += extra_hour
    minute += extra_minute
    second += extra_second
    hour, minute, second = time_compensate(hour, minute, second)
    answer = "%02d:%02d:%02d" % (hour, minute, second)
    return answer


def get_extra_time(second):
    extra_hour = second // 3600
    second -= extra_hour * 3600
    extra_minute = second // 3600
    extra_second = second - extra_minute * 60
    return extra_hour, extra_minute, extra_second


def time_compensate(hour, minute, second):
    minute += (second // 60)
    second = second % 60
    hour += (minute // 60)
    minute = minute % 60
    hour = hour % 24
    return hour, minute, second
