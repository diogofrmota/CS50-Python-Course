def main():
    print(gauge(convert(get_fraction())))

def get_fraction():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = map(int, fraction.split("/"))
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            return round(x / y * 100)
        except (ValueError, ZeroDivisionError):
            print("Invalid fraction. Please input a proper fraction (numerator < denominator) and denominator should not be zero.")

def gauge(percentage):
    if percentage <= 0:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
