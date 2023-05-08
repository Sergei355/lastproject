class Laptop:

    def __init__(self, brand='no name', model='no name', price=1):
        self.__brand = brand
        self.__model = model
        self.__price = price

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, int) and 0 < price:
            self.__price = price

    def __str__(self):
        return f"{self.__brand}, {self.__model} with price: {self.__price}"
