if __name__ == "__main__":
    ascending = [1, 2, 3, 4, 5, 6, 7, 8]

    sequence = list(map(int, input().split()))

    if sequence == ascending:
        print("ascending")
    elif sequence == ascending[::-1]:
        print("descending")
    else:
        print("mixed")