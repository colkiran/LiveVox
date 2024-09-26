
from collections import namedtuple

def arithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    mod = x % y
    nmdTpl = namedtuple("Arithmetic", "s d p q m")
    ntpl = nmdTpl(s = sum, d = diff, p = prod, q = quot, m = mod)
    return ntpl

arith = arithmeticCalc(20, 8)
print(arith)
print(f"Sum  :{arith.s}")
print(f"Diff :{arith.d}")
print(f"Prod :{arith.p}")
print(f"Quot :{arith.q}")
print(f"Mod  :{arith.m}")

