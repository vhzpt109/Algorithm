from string import ascii_lowercase

if __name__ == "__main__":
    word = input().lower()

    alphabet_list = list(ascii_lowercase)
    count_alphabet_list = []

    for alphabet in alphabet_list:
        count_alphabet_list.append(word.count(alphabet))

    max_index = count_alphabet_list.index(max(count_alphabet_list))

    count_alphabet_list.sort(reverse=True)

    if count_alphabet_list[0] == count_alphabet_list[1]:
        print("?")
    else:
        print(str(alphabet_list[max_index]).upper())