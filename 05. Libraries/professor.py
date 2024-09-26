from random import randint

def main():
    """Main function runs the game."""
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        score += check_answer(x, y)
    print("Score:", score)

def get_level():
    """Prompt the user for a level between 1-3. Keeps asking until a valid level is entered."""
    while True:
        try:
            level = int(input("Enter a level between 1-3: "))
            if level in [1, 2, 3]:
                return level
            print("Invalid level. Please enter a level between 1-3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_integer(level):
    """Generate an integer based on the level."""
    if level == 1:
        return randint(0, 9)
    return randint(10 ** (level - 1), 10**level - 1)

def check_answer(x, y):
    """Prompt the user for the sum of x and y. User has three tries."""
    tries = 0
    while tries < 3:
        try:
            tries += 1
            answer = int(input(f"{x} + {y} = "))
            if answer == x + y:
                return 1
            else:
                print("Incorrect. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    print(f"The correct answer was {x} + {y} = {x + y}")
    return 0

if __name__ == "__main__":
    main()
