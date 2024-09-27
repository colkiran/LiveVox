"""
def outerFun():
    gname = "Sachin"
    def innerFun():
        nonlocal gname
        print("Hello World")
        gname = "hello"
        print(f"greet Mr.{gname}")

    innerFun()
    print(gname)

outerFun()

"""
a = 10
def f1():
    global a
    x = 10

    def f2():
        y = 20
        nonlocal x
        x = 500
        print(f"inside :{y}")
        a = 250
        print(f"inside :{a}")

    f2()
    print(f"outside :{x}")
    print(f"outside :{a}")


f1()
