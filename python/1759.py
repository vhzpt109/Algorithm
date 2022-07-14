vowel = ["a", "e", "i", "o", "u"]

def dfs(password_list, alphabet_list, idx, password, depth):
    if depth == l:
        vowel_count = 0
        consonant_count = 0
        for char in password:
            if char in vowel:
                vowel_count += 1
            else:
                consonant_count += 1
        if vowel_count < 1 or consonant_count < 2:
            return
        else:
            print("".join(password))
            return

    for i in range(idx, c):
        if alphabet_list[i] not in password:
            password.append(alphabet_list[i])
            dfs(password_list, alphabet_list, i + 1, password, depth + 1)
            password.pop()


if __name__ == "__main__":
    l, c = map(int, input().split())
    alphabet_list = list(map(str, input().split()))
    alphabet_list.sort()

    password_list = []

    dfs(password_list, alphabet_list, 0, [], 0)