import math

if __name__ == "__main__":
    n = int(input())
    m_list = []

    for _ in range(n):
        m_list.append(int(input()))
    m_list.sort()

    m_diff_list = []
    for i in range(len(m_list) - 1):
        m_diff_list.append(abs(m_list[i] - m_list[i + 1]))

    gcd = m_diff_list[0]
    for i in range(1, len(m_diff_list)):
        gcd = math.gcd(gcd, m_diff_list[i])

    divisor_list = []
    for i in range(2, int(math.sqrt(gcd)) + 1):
        if gcd % i == 0:
            divisor_list.append(i)
            divisor_list.append(gcd // i)
    divisor_list.append(gcd)

    divisor_list = list(set(divisor_list))
    divisor_list.sort()

    for divisor in divisor_list:
        print(divisor, end=" ")