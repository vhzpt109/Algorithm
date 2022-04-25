import sys

if __name__ == "__main__":
    k = int(sys.stdin.readline())

    money_book = []
    for _ in range(k):
        money = int(sys.stdin.readline())
        if money == 0:
            money_book.pop()
        else:
            money_book.append(money)

    print(sum(money_book))