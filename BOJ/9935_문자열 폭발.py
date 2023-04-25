if __name__ == "__main__":
    _string = input().rstrip()
    explosion_string = input().rstrip()

    overlab_count_stack = []
    final_string = []

    for i in range(len(_string)):
        if _string[i] == explosion_string[0]:
            for j in range(len(explosion_string[1:])):
                if _string[i + j] != explosion_string[j]:
                    break
                else:
                    overlab_count_stack.append(1)
                    final_string.append(_string[i + j])

    if len(final_string) == 0:
        print("FRULA")
    else:
        for c in final_string:
            print(c, end="")