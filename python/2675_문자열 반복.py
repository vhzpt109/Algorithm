if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        r, s = map(str, input().split(" "))
        for text in s:
            for _ in range(int(r)):
                print(text, end="")
        print("")  # 개행
