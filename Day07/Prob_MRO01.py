class A:
    def disp(self):
        print("Greetings from Class A")

class B:
    def disp(self):
        print("Greetings from Class B")

class C(A, B):
    pass

objC = C()
objC.disp()



