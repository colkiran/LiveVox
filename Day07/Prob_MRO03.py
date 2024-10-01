
class A:

    def disp(self):
        print("Greetings from class A")


class B(A):
   pass


class C(A):

    def disp(self):
        print(f"Greetings from class C")


class D(B, C):
    pass


objD = D()
objD.disp()

print("-" * 60)
print(D.mro())
