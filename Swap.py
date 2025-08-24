a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swap: a =", a, "b =", b)

a, b = b, a   # swap in one line

print("After swap: a =", a, "b =", b)
