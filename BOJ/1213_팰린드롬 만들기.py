from string import ascii_uppercase


if __name__ == "__main__":
    name = input().rstrip()
    name_alphabet_count_list = []

    alphabet_list = list(ascii_uppercase)
    for alphabet in alphabet_list:
        name_alphabet_count_list.append(name.count(alphabet))

    center_alphabet = ""
    for i in range(len(name_alphabet_count_list)):
        if name_alphabet_count_list[i] % 2 != 0:
            center_alphabet += alphabet_list[i]

        if len(center_alphabet) > 1:
            print("I'm Sorry Hansoo")
            exit(0)

    palindrome = ""
    for i in range(len(name_alphabet_count_list)):
        palindrome += alphabet_list[i] * (name_alphabet_count_list[i] // 2)

    print(palindrome + center_alphabet + palindrome[::-1])