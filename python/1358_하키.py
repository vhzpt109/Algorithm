if __name__ == "__main__":
    w, h, x, y, p = map(int, input().split())
    r = int(h / 2)
    player_count = 0

    for _ in range(p):
        px, py = map(int, input().split())

        if r**2 >= (x - px)**2 + (y + r - py)**2:
            player_count += 1
        elif r**2 >= (x + w - px)**2 + (y + r - py)**2:
            player_count += 1
        elif x <= px <= x + w and y <= py <= y + h:
            player_count += 1
    print(player_count)