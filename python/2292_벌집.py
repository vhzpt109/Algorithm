if __name__ == "__main__":
    n = int(input())

    num_room = 1
    cnt = 1
    while n > num_room:
        num_room += cnt * 6
        cnt += 1
    print(cnt)