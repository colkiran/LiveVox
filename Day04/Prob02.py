def fib(n):
    if n == 0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)

x= int (input("Enter the number of iterations : "))
for i in range(x):
    print (fib(i),end=" ")