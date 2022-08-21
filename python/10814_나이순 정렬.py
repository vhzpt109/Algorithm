import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    member_list = []
    for _ in range(n):
        age, name = map(str, sys.stdin.readline().split())
        member_list.append((int(age), name))
    member_list.sort(key=lambda age:age[0])

    for member in member_list:
        print(member[0], member[1])