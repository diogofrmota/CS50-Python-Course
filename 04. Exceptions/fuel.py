while True:
    try:
        x, y = map(int, input("Enter the fraction (format like X/Y): ").split("/"))
        if y == 0:
            raise ZeroDivisionError("Denominator cannot be zero!")
        if x > y:
            raise ValueError("Numerator can't be higher than the denominator!")
        break
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)

percentage = round(x / y * 100)
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
