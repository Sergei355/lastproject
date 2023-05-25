from transport import Transport


class Electrocars(Transport):

    def __init__(self, brand='no name', model='no name', price=1, battery_charge=100):
        super().__init__(brand, model, price)
        self.__battery_charge = battery_charge

        @property
        def battery_charge(self):
            return self.__battery_charge

        @battery_charge.setter
        def battery_charge(self, battery_charge):
            self.__battery_charge = battery_charge

        def __str__(self):
            return (super().__str__()
                    + f" have battery charge: {self.__battery_charge} km.")
