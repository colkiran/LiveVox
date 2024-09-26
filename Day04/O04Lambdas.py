
def add(x, y):
    return x + y

a = add

res = a(37, 84)
print(f"res :{res}")

print("-" * 60)

b = lambda x, y: x + y

res = b(54, 39)
print(f"res :{res}")


print("-" * 60)
# lambda is best used with - map, filter, reduce
l1 = list(range(1, 11))
print(f"l1 :{l1}")

# map
squares = list(map(lambda x : x ** 2, l1))
print(f"squares :{squares}")

# conversions = dollars - rupees, pounds - kgs, litres - gallons

months = ['apr', 'aug', 'dec', 'sep', 'jan', 'oct', 'mar', 'nov', 'feb', 'jul', 'may', 'jun']
# sort these months - sorted function
print(f'unsorted months :{months}')


print("-" * 60)
from calendar import month_abbr, month_name
print(list(month_abbr))

print("-" * 60)
print("-" * 60)
sorted_months = sorted(months, key=list(map(lambda mth : mth.lower(), list(month_abbr))).index)
print(f"Sorted Months :{sorted_months}")

# res = sorted(cities, key=len)

print("-" * 60)
print(list(month_name))

sorted_months = sorted(months, key=list(map(lambda mth : mth[0:3].lower(), list(month_name))).index)

print("-" * 60)
# filters

l1 = list(range(1, 31))
print(f"l1 :{l1}")

mul_three = list(filter(lambda x : x % 3 == 0, l1))
print(mul_three)
print("-" * 60)

sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

print("-" * 60)
res = list(filter(lambda x : x != 'the', sentence.split()))
print(f"res :{res}")

print("-" * 60)
# reduce

from functools import reduce
l1 = [8, 6, 3, 9, 5, 7, 10, 4]
print(f"l1 :{l1}")

res = reduce(lambda x, y: x if x > y else y, l1)
print(f"res :{res}")

res1 = reduce(lambda x, y: x + y, l1)
print(f"res1 :{res1}")