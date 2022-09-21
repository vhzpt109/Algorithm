def star(n, star_list):
    out = []
    if n == 3:
        return star_list
    else:
        for i in star_list:
            out.append(i * 3)
        for i in star_list:
            out.append(i + ' ' * len(star_list) + i)
        for i in star_list:
            out.append(i * 3)
        return star(n//3, out)


if __name__ == "__main__":
    n = int(input())
    star_list = ["***", "* *", "***"]
    result = star(n, star_list)
    for i in result:
        print(i)