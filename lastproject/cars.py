from transport import Transport


class Cars(Transport):

    def __init__(self, brand='no name', model='no name', price=1, engine_capacity=2, fuel_consumption=5):
        super().__init__(brand, model, price)
        self.__engine_capacity = engine_capacity
        self.__fuel_consumption = fuel_consumption

        @property
        def engine_capacity(self):
            return engine_capacity

        @property
        def fuel_consumption(self):
            return fuel_consumption

        @engine_capacity.setter
        def engine_capacity(self, engine_capacity):
            self.__engine_capacity = engine_capacity

        @fuel_consumption.setter
        def fuel_consumption(self, engine_capacity):
            self.__fuel_consumption = fuel_consumption

        def __str__(self):
            return (super().__str__()
                    + f" have engine capacity: {self.__engine_capacity} with fuel consumption"
                      f": {self.__fuel_consumption}.")
