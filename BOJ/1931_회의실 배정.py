import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    meeting_infomation = []
    for _ in range(n):
        start_time, end_time = map(int, sys.stdin.readline().rstrip().split())
        meeting_infomation.append((start_time, end_time))
    meeting_infomation.sort(key=lambda x: x[0])
    meeting_infomation.sort(key=lambda x: x[1])

    meeting_count = 0
    previous_meeting_end_time = 0
    for meeting in meeting_infomation:
        if meeting[0] >= previous_meeting_end_time:
            meeting_count += 1
            previous_meeting_end_time = meeting[1]
    print(meeting_count)