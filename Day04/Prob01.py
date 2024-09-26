
def fact(x):
    if x==1 or x==0:
        return 1
    else :
        return x * fact(x-1)


n = int(input("Enter a number to find its Factorial :"))
print(f"The factorial of {n} is {fact(n)}")
