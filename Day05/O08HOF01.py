
def fun(*args):
    print(args)

fun()
fun(10)
fun(10, 20)
fun(10, 20, 30)

print("=" * 60)

def add(x, y):
    return x + y

def outerFun(fnc):

    def innerFun(*args):
        print("Logging into a resource.......")
        print(fnc(*args))              # call back
        print("-" * 60)

    return innerFun

addLogger = outerFun(add)
addLogger(10, 20)