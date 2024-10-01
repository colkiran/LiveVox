import dis


class A:
    def disp(self):
        print("Greetings from Class A")

class B:
    def disp(self):
        print("Greetings from Class B")

class C(A, B):

    def disp(self):
        print("Greetings from Class C")


class D(C, B):
    pass


objD = D()
objD.disp()

print("-" * 60)

print(D.mro())

"""

D->B->C->B->A
D->C->B->A ->B
"""