def main():
    time = int(input("What's the time? "))
    if 6 <= time <= 10:
        print("Breakfast time")
    elif 11 <= time <= 14:
        print("Lunch time")
    elif 18 <= time <= 22:
        print("Dinner time")
    else:
        print("Hora de passar fome")


def convert(time):
    hours, minutes = map(int, time.replace("a.m.", "").replace("p.m.", "").split(":"))
    if "p.m." in time and hours != 12:
        hours += 12
    if "a.m." in time and hours == 12:
        hours = 0
    return hours + minutes / 60


main()