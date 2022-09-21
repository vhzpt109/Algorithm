import math

if __name__ == "__main__":
    n = int(input())
    r_list = list(map(int, input().split()))

    for r in r_list[1:]:
        gcd = math.gcd(r_list[0], r)
        print(str(r_list[0] // gcd) + "/" + str(r // gcd))