
class Arithmetic:

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num
    def __truediv__(self, other):
        return self.num / other.num
    def __floordiv__(self, other):
        return self.num // other.num
    def __mod__(self, other):
        return self.num % other.num


num1 = Arithmetic(50)
num2 = Arithmetic(10)
print(f"num1 + num2 = {num1+num2}")
print(f"num1 - num2 = {num1-num2}")
print(f"num1 * num2 = {num1*num2}")
print(f"num1 % num2 = {num1%num2}")
print(f"num1 // num2 = {num1//num2}")
print(f"num1 / num2 = {num1/num2}")

