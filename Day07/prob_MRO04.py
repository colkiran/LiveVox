
class A:

    def disp(self):
        print("Greetings from class A")


class B(A):

    def disp(self):
        print("Greetings from class B")


class C(A, B):
    pass


objC = C()
objC.disp()

"""
<class '__main__.C'> <class '__main__.A'> <class '__main__.B'> <class '__main__.A'>


C->B->A

C->A->B->A
"""