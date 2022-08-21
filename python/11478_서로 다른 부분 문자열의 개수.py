if __name__ == "__main__":
    s = input()
    result_set = set()

    for i in range(len(s)):
        for j in range(i, len(s)):
            result_set.add(s[i:j+1])
    print(len(result_set))