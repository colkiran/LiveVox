
def outerFun():             # HOF - higher order function
    gname = "Sachin"

    def innerFun():

        print("Hello World")
        print(f"Hello {gname}")

    return innerFun

inref = outerFun()

print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")

print("-" * 60)
inref()