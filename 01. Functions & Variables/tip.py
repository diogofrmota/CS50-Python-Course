def main():
    dollars = float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def percent_to_float(p):
    return float(p.strip('%')) / 100


main()