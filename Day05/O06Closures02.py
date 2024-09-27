
def outerFun(greet):

    # simple curry
    def innerFun(gname):

        print(greet, gname)

    return innerFun


EngGrt = outerFun("Hello")
KanGrt = outerFun("Namaskara")

EngGrt("Sachin")
EngGrt("Sourav")
EngGrt("Sehwag")

print("-" * 60)

KanGrt("Rahul")
KanGrt("Kumble")
KanGrt("Srinath")
