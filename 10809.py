from string import ascii_lowercase

if __name__ == "__main__":
    s = input()

    alphabet_list = list(ascii_lowercase)
    index_alphabet_list = []

    for alphabet in alphabet_list:
        index_alphabet_list.append(s.find(alphabet))

    for index_alphabet in index_alphabet_list:
        print(index_alphabet, end=" ")