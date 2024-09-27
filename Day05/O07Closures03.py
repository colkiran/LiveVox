import emojis


def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):
            from emojis import emojis

            emojized = emojis.encode(greet + " :" + sep + ": " + gname)

            print(emojized)

        return innerMostFun

    return innerFun

KanGrt = outerFun("Namaskara")

KanGrtTiger = KanGrt("tiger")
KanGrtLion = KanGrt("lion")

KanGrtTiger("Prabhakar")
KanGrtLion("Vishuvardhan")


"""
EngGrt =  outerFun("Hello")

EgnGrtSngArw = EngGrt("------>")
EgnGrtDblArw = EngGrt("======>>")


EgnGrtSngArw("Sachin")
EgnGrtDblArw("Sachin")

"""