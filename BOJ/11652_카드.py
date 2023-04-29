if __name__ == "__main__":
    n = int(input())
    num_list = []
    hash_table = {}

    for _ in range(n):
        num_list.append(int(input()))
    num_list.sort(reverse=True)

    for i in range(n):
        match = hash_table.get(num_list[i])
        if match is None:
            hash_table[num_list[i]] = 1
        else:
            hash_table[num_list[i]] += 1

    max_key = 0
    max_value = -1
    for key, value in hash_table.items():
        if value >= max_value:
            max_value = value
            max_key = key

    print(max_key)