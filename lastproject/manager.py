from transport import Transport
from cars import Cars
from minibuses import Minibuses
from electrocars import Electrocars
from trucks import Trucks


class Manager:

    @staticmethod
    def find_max_price_taxopark1(taxopark1):

        target = taxopark1[0]

        for car in taxopark1:
            if car.price > target.price:
                target = car
        return target

    @staticmethod
    def find_max_price_taxopark2(taxopark2):

        target = taxopark2[0]

        for car in taxopark2:
            if car.price > target.price:
                target = car
        return target

    @staticmethod
    def find_min_price_taxopark1(taxopark1):

        target = taxopark1[0]

        for car in taxopark1:
            if car.price > target.price:
                target = car
        return target

    @staticmethod
    def find_min_price_taxopark2(taxopark2):

        target = taxopark2[0]

        for car in taxopark2:
            if car.price > target.price:
                target = car
        return target

    @staticmethod
    def find_general_price_taxopark1(taxopark1):

        general_price = len(taxopark1)
        target = 0

        for car in range(general_price):
            target.price = target.price + taxopark1[car]

        return target

    @staticmethod
    def find_big_taxopark(self, taxopark1, taxopark2):

        result = sum(taxopark1) if sum(taxopark1) > sum(taxopark2) else sum(taxopark2)

        return result
