if __name__ == "__main__":
    word = input()

    croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    for i in croatia_alphabet:
        word = word.replace(i, '*')

    print(len(word))