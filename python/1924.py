from datetime import date

if __name__ == "__main__":
    x, y = map(int, input().split())

    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = date(2007, x, y).weekday()
    print(days[day])