"""
arithmetic
augmentor
comparison
logical
bitwise
ternary
"""

print("Arithmetic Operator".center(60, "-"))
print(f"Add : 5 + 3 = {5 + 3}")
print(f"Sub : 5 - 3 = {5 - 3}")
print(f"Mul : 5 * 3 = {5 * 3}")
print(f"Div : 5 / 3 = {5 / 3}")
print(f"Flr Div : 5 // 3 = {5 // 3}")
print(f"mod : 5 % 3 = {5 % 3}")
print(f"Exp : 5 ** 3 = {5 ** 3}")

print("Augmentor Operators".center(60, "-"))
# =, +=, -=, *=, /=
x = 5
print(f"x :{x}")

x *= 3    # x = x * 3
print(f"x :{x}")

x /= 3
print(f"x :{x}")

x += 1
print(f"x :{x}")

print("Comparison Operator".center(60, "-"))
# ==, >, <, >=, <=, !=
x = 10
y = 15

print(x, y, sep=", ")
print(f"x == y :{x == y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x != y: {x != y}")

print("Logical Operator".center(60, "-"))
# and, or, not

print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 1 and 2 == 1 :{1 == 1 and 2 == 1}")

print('-' * 60)
print(f"1 == 2 or 2 == 1 :{1 == 2 or 2 == 1}")
print(f"1 == 1 or 2 == 1 :{1 == 1 or 2 == 1}")

print('-' * 60)
print(f"not(1 == 2 or 2 == 1) :{not(1 == 2 or 2 == 1)}")
print(f"not(1 == 1 or 2 == 1) :{not(1 == 1 or 2 == 1)}")

print("Bitwise Operators".center(60, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 >> 1 :{5 >> 1}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"16 >> 1 :{16 >> 1}")

print("Ternary Operator".center(60, "-"))
age = 18
print("Eligible" if age > 17 else "Not Eligible")
