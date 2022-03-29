if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    if len(numbers) > n:
        exit()
    numbers.sort()
    print(numbers[0], numbers[-1])