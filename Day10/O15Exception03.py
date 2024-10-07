
class ThreeDivisionError(Exception):
    def __init__(self):
        print("ThreeDivisionError Ctor.....")
        print("Number cannot be divided by three......")


num1 = int(input("Enter the numerator :"))
num2 = int(input("Enter the denaminator :"))

try:
    if num2 == 3:
        raise ThreeDivisionError
        # raise ThreeDivisionError("Cannot divide by 3.....")

    res = num1 / num2           # suspicious code
    print(f"res :{res}")
except ThreeDivisionError as x:
    print(x)

print("rest of the code....")