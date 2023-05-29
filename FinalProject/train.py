

class Train:
    def __init__(self, wagon=1, passenger_seat=1, wagon_length=1000, baggage_weight=2000):
        self.__passenger_seat = passenger_seat
        self.__wagon_length = wagon_length
        self.__baggage_weight = baggage_weight
        self.__wagon = wagon

    @property
    def wagon(self):
        return self.__wagon

    @property
    def baggage_weight(self):
        return self.__baggage_weight

    @property
    def wagon_length(self):
        return self.__wagon_length

    @property
    def passenger_seat(self, passenger_seat):
        return self.__passenger_seat

    @wagon.setter
    def wagon(self, wagon):
        self.__wagon = wagon

    @baggage_weight.setter
    def baggage_weight(self, baggage_weight):
        self.__baggage_weight = baggage_weight

    @wagon_length.setter
    def wagon_length(self, wagon_length):
        self.__wagon_length = wagon_length

    @passenger_seat.setter
    def passenger_seat(self, passenger_seat):
        self.__passenger_seat = passenger_seat

    def __str__(self):
        return (f"Train: wagon = {self.__wagon}, "
                f"passenger_seat = {self.__passenger_seat}, "
                f"baggage_weight = {self.__baggage_weight}, "
                f"wagon_length = {self.__wagon_length}")



