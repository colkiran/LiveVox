
class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        print("getter called.....")
        return self.__price

    @price.setter
    def price(self, prc):
        print("Setter called.....")
        self.__price = prc

    @price.deleter
    def price(self):
        print("deleter called.......")
        self.__price = 0




pepsi = Product(100)
print(pepsi.price)

pepsi.price = 120
print(pepsi.price)

del pepsi.price                 # deleter
print(pepsi.price)

