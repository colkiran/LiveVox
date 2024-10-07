"""
every error of exception bound with a class

ZeroDivisionError


What are exceptions?
if the error is triggered then will not stop the execution of the code.


try:
    error prone code

except class:

else:

finally:

"""

num1 = int(input("Enter the numerator :"))
num2 = int(input("Enter the denaminator :"))

try:
    res = num1 / str(num2)           # suspicious code

# except ZeroDivisionError as e:
#     print("Exception occured.....")
#     print(e)
#     # print("cannot have the denominator as zero....")
#
# except ValueError as v:
#     print("Exception occured.....")
#     print(v)

except (ZeroDivisionError, TypeError) as x:
    print(x)
else:
    print(f"res :{res}")

finally:
    print("completed division of numbers")

print("rest of code......")