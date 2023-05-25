from cars import Cars


class Minibuses(Cars):

    def __init__(self, brand='no name', model='no name', price=1, engine_capacity=2,
                 fuel_consumption=5, body_volume=30):
        super().__init__(brand, model, price, engine_capacity, fuel_consumption)
        self.__body_volume = body_volume

    @property
    def body_volume(self):
        return self.__body_volume

    @body_volume.setter
    def body_volume(self, body_volume):
        self.__body_volume = body_volume

    def __str__(self):
        return (super().__str__()
                + f"The body of this model is: {self.__body_volume}.")
