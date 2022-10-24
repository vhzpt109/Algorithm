if __name__ == "__main__":
    student_list = []
    for _ in range(28):
        student_list.append(int(input()))
    student_list.sort()

    for i in range(1, 31):
        if student_list.count(i) == 0:
            print(i)