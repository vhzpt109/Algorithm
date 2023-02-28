if __name__ == "__main__":
    score = 0
    credits = []
    grade_table = {"A+": 4.5,
                   "A0": 4.0,
                   "B+": 3.5,
                   "B0": 3.0,
                   "C+": 2.5,
                   "C0": 2.0,
                   "D+": 1.5,
                   "D0": 1.0,
                   "F": 0.0}
    for _ in range(20):
        subject_name, credit, grade = map(str, input().split())
        if grade == "P":
            continue

        score += (float(credit) * grade_table[grade])
        credits.append(float(credit))

    print(score / sum(credits))

