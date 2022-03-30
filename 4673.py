def d():
    number = set(range(1, 10001))
    s = set()

    for i in range(1, 10001):
        for j in str(i):
            i += int(j)
        s.add(i)

    self_number = sorted(number - s)

    for i in self_number:
        print(i)

if __name__ == "__main__":
    d()