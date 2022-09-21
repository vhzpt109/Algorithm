import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    number_list = list(map(int, sys.stdin.readline().split()))
    number_list_sorted = sorted(set(number_list))

    number_dict = {}
    for i in range(len(number_list_sorted)):
        number_dict[number_list_sorted[i]] = i

    for number in number_list:
        print(number_dict[number], end=" ")