if __name__ == "__main__":
    s = input().rstrip()

    s_split0 = s.split("0")
    s_split0 = [c for c in s_split0 if c != '']

    s_split1 = s.split("1")
    s_split1 = [c for c in s_split1 if c != '']

    print(min(len(s_split0), len(s_split1)))