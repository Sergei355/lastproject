class Transport:

    def __init__(self, brand='no name', model='no name', price=1):
        self.__brand = brand
        self.__model = model
        self.__price = price if price > 0 else 1

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
        if price > 0:
            self.__price = price

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @model.setter
    def model(self, model):
        self.__model = model

    def __str__(self):
        return f"{self.__brand}, {self.__model} with price: {self.__price}$."
