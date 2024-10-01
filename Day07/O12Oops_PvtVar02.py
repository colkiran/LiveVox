
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return f"price is {self.__price}"

    def set_price(self, prc):
        if prc < 0:
            raise ValueError("Price cannot be less than zero.....")
        else:
            self.__price = prc


    def del_price(self):
        self.__price = 0

import sys

try:
    pepsi = Product(45)
    print(pepsi.get_price())            # method

    pepsi.set_price(50)
    print(pepsi.get_price())

    pepsi.del_price()
    print(pepsi.get_price())


except:
    print("Exception raised....")

    print(sys.exc_info()[0])            # class name
    print(sys.exc_info()[1])            # message


finally:

    print("Product price manipulated successfully......")
