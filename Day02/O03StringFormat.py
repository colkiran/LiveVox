
# c Style formatting
format = "Welcome %s, what a %s player"
values = ("Sachin", "superb")
print(format, values)

print(format % values)
print("-" * 60)

print("Welcome %s, what a %s player" % ("Sachin", "superb"))
print("Welcome %s, what a %s player with a rating %d" % ("Sachin", "superb", 9))
print("Welcome %s, what a %s player with a rating %.2f" % ("Sachin", "superb", 9.8765))

print("-" * 60)
# python formating
print("Welcome {}, what a {} player".format("Sachin", "class"))
print("Welcome {plyr}, what a {adj} player with a rating {rt}".format(plyr = "Sachin", adj = "class", rt=9))
print("Welcome {plyr}, what a {adj} player with a rating {rt:.2f}".format(plyr = "Sachin", adj = "class", rt=9.8765))

print("-" * 60)
# conversions
print("{val} {val} {val}".format(val="A"))
print("{val!s} {val!r} {val!a}".format(val="A"))

print("{num} {num} {num}".format(num = 36))
print("{num} {num:f} {num:b}".format(num = 36))
print("{num:10} {num:f} {num:b}".format(num = 36))
print("{num:5} {num:f} {num:b}".format(num = 36))
print("{num:5} {num:f} {num:b}".format(num = 362987612))

print("-" * 60)
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))
from math import pi

print("{pi}".format(pi=pi))
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

print("-" * 60)
# alignment
print("{:>15} Tendulkar".format("Sachin"))       # right alignment
print("{:^15} Tendulkar".format("Sachin"))       # center alignment
print("{:<15} Tendulkar".format("Sachin"))       # left alignment

print("{:08} runs".format(100))
print("{:-^60}".format("Python"))
print("Python".center(60, "-"))
