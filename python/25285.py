if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        cm, kg = map(int, input().split())
        bmi = kg / (cm / 100.)**2

        if cm < 140.1:
            print(6)
        elif 140.1 <= cm < 146.:
            print(5)
        elif 146. <= cm < 159.:
            print(4)
        elif 159. <= cm < 161.:
            if 16.0 <= bmi < 35.:
                print(3)
            else:
                print(4)
        elif 161. <= cm < 204.:
            if 20.0 <= bmi < 25.:
                print(1)
            elif 18.5 <= bmi < 20. or 25. <= bmi < 30.:
                print(2)
            elif 16. <= bmi < 18.5 or 30. <= bmi < 35.:
                print(3)
            else:
                print(4)
        elif 204. <= cm:
            print(4)