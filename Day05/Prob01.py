import time
st = time.perf_counter()


def timcal(fnc):

    def helperfunc(x):
        print("Function executing.......")
        st = time.perf_counter()
        fnc(x)
        et = time.perf_counter()
        print("Completed excution.........")
        print(f"time taken : {round(et - st, 2)}")

    return helperfunc

@timcal
def fun(n):
    lst = []
    for i in range(n):
        for j in range(1, i+1):
            lst.append(j ** 3)


fun(7000)