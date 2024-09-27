
from datetime import datetime

date = datetime.now()
print(f"date :{date}")

print("-" * 60)
print(f"Day :{date.strftime('%a')}")
print(f"Day :{date.strftime('%A')}")

print("-" * 60)
print(f"Month :{date.strftime('%b')}")
print(f"Month :{date.strftime('%B')}")

print("-" * 60)
print(f"Date :{date.strftime('%d')}")
print(f"Date :{date.strftime('%D')}")
print(f"Date :{date.strftime('%x')}")

print("-" * 60)
print(f"Year :{date.strftime('%y')}")
print(f"Year :{date.strftime('%Y')}")

print("-" * 60)
print(f"Time :{date.strftime('%T')}")
print(f"Time :{date.strftime('%X')}")

print("-" * 60)
dt1 = date.strftime("%d-%m-%y")
print(f"dt1 :{dt1}")
print(type(dt1))

print("-" * 60)
dt2 = date.strftime("%d-%m-%Y")
print(f"dt2 :{dt2}")

print("-" * 60)
dt3 = date.strftime("%d-%b-%Y")
print(f"dt3 :{dt3}")

print("-" * 60)
dt4 = date.strftime("%d-%B-%Y")
print(f"dt4 :{dt4}")

