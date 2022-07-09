if __name__ == "__main__":
    score_list = []
    for _ in range(5):
        score = int(input())
        score = 40 if score < 40 else score
        score_list.append(score)
    print(int(sum(score_list) / 5.))