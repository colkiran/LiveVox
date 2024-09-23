
"""
int
float
complex

"""

a = 10
b = -10

print(f"a :{a}")        # interpolation
print(type(a))          # RTTI - runtime type identification
print(f"b :{b}")
print(type(b))

print("-" * 60)
c = 100.0
d = -100.0

print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 60)
e = 2e3
f = -2e3

print(f"e :{e}")
print(type(e))

print(f"f :{f}")
print(type(f))

print("-" * 60)
g = 2 + 3j
h = 9 - 2j

print(f"g :{g}")
print(type(g))

print(f"h :{h}")
print(type(h))

print("-" * 60)
i = True
j = False

print(i)
print(type(i))
print(j)
print(type(j))

print("-" * 60)
print(max(5, 8, 3, 9, 4, 6 ))
print(min(5, 8, 3, 9, 4, 6 ))

print("-" * 60)

x =  3 + 2.5
print(type(x))

x = 2.5
y = 3
z = x + y

print("x = ", type(x))
print("Y = ", type(y))
print("z = ", type(z))

print("Conversion".center(60,"-"))
x = 100
print(f"{type(x)}\t\t{x}")
print(f"{type(float(x))}\t\t{float(x)}")
print(f"{type(complex(x))}\t\t{complex(x)}")
print(f"{type(bool(x))}\t\t{bool(x)}")


print("Number System".center(60, "-"))
print(11)           # decimal numbers
print(0b101)        # binary
print(0b11)         # binary
print(0o11)         # octal
print(0o101)        # octal
print(0xa)          # hexa
print(0xe)          # hexa

print("Number System Conversion".center(60, "-"))
a = 100
print(bin(a))
print(oct(a))
print(hex(a))

