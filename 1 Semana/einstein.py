'''
Anotações

print("Hello, word")

name = input("What's your name? ")

name = name.strip().title()

print(f"Hello, {name}")

x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)

float para numeros por exemplo 1.2, 2.7

E se quiser aredondar o número para o integer mais proximo? ou seja 2.3 fica 2 usar round()

z = round(x / y, 2)

def hello(to):
    print("Hello,", to)

name = input("What's your name? ")
hello(name)
'''

def compute(m, c=300000000):
    return m * c * c


print("E=", compute(int(input("m: "))))