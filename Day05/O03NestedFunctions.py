
def outerFun():
    gname = "Sachin"
    def innerFun():

        print("Hello World")
        print(f"Hello {gname}")

    innerFun()

outerFun()
