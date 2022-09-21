if __name__ == "__main__":
    n = int(input())

    list_rank = [1] * n

    list_kg_cm = []
    for _ in range(n):
        list_kg_cm.append(input().split())

    list_kg_cm = [list(map(int, i)) for i in list_kg_cm] # 2d string array to 2d int array

    for i in range(len(list_kg_cm)):
        kg_i = list_kg_cm[i][0]
        cm_i = list_kg_cm[i][1]
        for j in range(len(list_kg_cm)):
            if i == j:
                continue
            kg_j = list_kg_cm[j][0]
            cm_j = list_kg_cm[j][1]

            if kg_i < kg_j and cm_i < cm_j:
                list_rank[i] += 1

    for rank in list_rank:
        print(rank, end=" ")