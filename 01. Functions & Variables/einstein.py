# Anotations
print("Hello, world")

name = input("What's your name? ")

# Strips extra spaces from the name and capitalizes it
name = name.strip().title()

print(f"Hello, {name}")

x = int(input("What's x? "))
y = int(input("What's y? "))

# Prints the sum of x and y
print(x + y)

# Floats are for numbers like 1.2 or 2.7

# If you want to round a number to its nearest integer, 
# like converting 2.3 to 2, use round()

z = round(x / y, 2)

def hello(to):
    # Displays a hello message to the given person
    print("Hello,", to)

name = input("What's your name? ")
hello(name)

def compute(m, c=300000000):
    # Computes E=mc^2
    return m * c * c

print("E=", compute(int(input("m: "))))
