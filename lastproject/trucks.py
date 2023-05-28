from minibuses import Minibuses


class Trucks(Minibuses):

    def __init__(self, brand='no name', model='no name', price=1, engine_capacity=2,
                 fuel_consumption=5, tent_volume=60):
        super().__init__(brand, model, price, engine_capacity, fuel_consumption)
        self.__tent_volume = tent_volume

        @property
        def tent_volume(self):
            return self.__tent_volume

        @tent_volume.setter
        def tent_volume(self, tent_volume):
            self.__tent_volume = tent_volume

        def __str__(self):
            return (super().__str__() + f" have tent volume: {self.__battery_charge} m3.")
