
try:
    age = int(input("Enter the age :"))
    if age < 0:
        raise ValueError("Invalid age....")
    print(f"Your age is :{age}")

except ValueError as v:
    print(v)
    print("Enter a valid age :")

print("rest of code.....")