import sys


def DiffStatus(team1, team2):
    team1_status = 0
    team2_status = 0
    for i in range(len(team1)):
        for j in range(len(team1)):
            team1_status += status[team1[i]][team1[j]]
            team2_status += status[team2[i]][team2[j]]
    return abs(team1_status - team2_status)


def dfs(team_start, target_n_team, depth):
    global min_diff_status

    if len(team_start) == target_n_team // 2:
        team_link = []
        for i in range(target_n_team):
            if i not in team_start:
                team_link.append(i)
        diff_status = DiffStatus(team_start, team_link)
        min_diff_status = min(min_diff_status, diff_status)
        return

    for i in range(depth, target_n_team):
        if i not in team_start:
            team_start.append(i)
            dfs(team_start, target_n_team, i + 1)
            team_start.remove(i)


if __name__ == "__main__":
    n = int(sys.stdin.readline())

    players = [i for i in range(n)]
    status = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    min_diff_status = sys.maxsize
    dfs([], len(players), 0)
    print(min_diff_status)