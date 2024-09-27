
def doubleMesh(fnc):
    def helper(*args):
        print("=" * 40)
        fnc(*args)  # callback
        print("#" * 40)
    return helper


def startSingle(fnc):
    def helper(*args):
        print("*" * 40)
        fnc(*args)  # callback
        print("_" * 40)
    return helper


@startSingle
@doubleMesh
def fun1():
    print("fun1 called")


@startSingle
@doubleMesh
def fun2(x):
    print("funx called", x)


@startSingle
@doubleMesh
def fun3(x, y):
    print("fun3 called", x, y)