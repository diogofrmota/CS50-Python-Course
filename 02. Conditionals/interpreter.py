x, y, z = input("Expressão: ").split()

x, z = int(x), int(z)
ans = eval(f"{x} {y} {z}")

print(f"{ans:.1f}")