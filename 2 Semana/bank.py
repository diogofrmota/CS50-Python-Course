'''
Notas

print("Hello world")

x = int(input("What's x?: "))
y = int(input("What's y?: "))
        
if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else:
    print("x is equal to y")

    x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

'''

amount = int(input("Greetings, how much do you have in your account? "))
request = int(input("How much do you want to withdraw? "))

if amount < request:
    print("You dont have enought money")
else:
    new_balance = amount - request
    print(f"You withdrawed {request} dollars and your new balance is {new_balance}")