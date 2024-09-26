
def greet():
    print("Greetings Mr.Sachin, Welcome to the event......")


def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.....")

# city is a default argument and gname is non default arg
def greetGstCty(gname, city = "Mumbai"):
    print(f"Greeting Mr.{gname} from {city}, Welcome to the event.......")


greet()

print("-" * 60)

greetGst("Sachin")
greetGst("Dhoni")

print("-" * 60)

greetGstCty("Rohit")
greetGstCty("Sunil")
greetGstCty("Rahul", "Bangalore")

print("-" * 60)

def admission(lname, fname, dob, qlf, city, gender, conno, address):
    print(f"Name          :{fname} {lname}")
    print(f"DOB           :{dob}")
    print(f"Qualification :{qlf}")
    print(f"City          :{city}")
    print(f"Gender        :{gender}")
    print(f"Contact No.   :{conno}")
    print(f"Address       :{address}")

admission(gender="female", conno="2878927", dob="10/05/1992", qlf="B.E", city="Bangalore", address="MG Road, Trinity Circle", lname="Singh", fname="Radha")


print("-" * 60)
# variable length argument - *args,  **kwargs



def prodAll(*numbers):
    print(f"numbers :{numbers}")
    print("*numbers :", *numbers)
    prod = 1
    for number in numbers:
        prod *= number  # prod = prod * number
    return prod

res = prodAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)
# **kwargs - accepts data like a dictionary
d1 = {"name": "Jack", "age" : 32, "desig" : "MGR", "dept":"Finance", "loc": "Mumbai"}

def extractDetails(**details):
    print(details)
    for k, v in details.items():
        print(k, "=>", v)

# extractDetails(name="Jack", age=32, desig="MGR", dept="Finance", loc="Mumbai")
extractDetails(**d1)


print("-" * 60)
# return


def multiplyMe(x, y):
    return x * y

print(f"The product of 5 and 6 is : {multiplyMe(5, 6)}")

# recursive calls - function calling itself
# 1. factorial of a number using recursive calls
# 2. fibonacci series using recursive calls

print("-" * 60)

def arithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    mod = x % y
    return sum, diff, prod, quot, mod

res = arithmeticCalc(20, 8)
print(f"res :{res}")

print("-" * 60)

def fun():
    # this is a comment
    "This is a doc string"
    print("Hello World")

fun()
print(fun.__doc__)

print("-" * 60)

def fun1(x, y):
    """
    fun1(x, y)
    ----------

    1. if x and y are integers then the result is the sum of the numbers
    2. if x and y are strings then the result is concatenation of x and y
    3. if x and y are of two different data type then it throws an error
    """
    return x + y


print(fun1(45, 92))
print(fun1("hello", " world"))

print("-" * 60)
help(fun1)
