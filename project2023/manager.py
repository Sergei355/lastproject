from transport import Transport


class Manager:

    @staticmethod
    def find_max_price_taxopark(taxopark):

        target = taxopark[0]

        for car in taxopark:
            if isinstance(car, Transport) and car.price > target.price:
                target = car

        return target

    @staticmethod
    def find_min_price_taxopark(taxopark):

        target = taxopark[0]

        for car in taxopark:
            if isinstance(car, Transport) and car.price < target.price:
                target = car
        return target.price

    @staticmethod
    def find_general_price_taxopark(taxopark):
        target = 0

        for car in taxopark:
            target = target + car.price

        return target

    @staticmethod
    def find_big_taxopark(taxopark1, taxopark2):
        count1 = Manager.__count(taxopark1)
        count2 = Manager.__count(taxopark2)

        result = count1 if count1 > count2 else count2

        return result

    @staticmethod
    def __count(taxopark):
        return len(taxopark) if isinstance(taxopark, list) else 0
