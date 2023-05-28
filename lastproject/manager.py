from transport import Transport

class Manager:

    @staticmethod
    def find_max_price(taxopark1):

        target = taxopark1[0]

        for car in taxopark1:
            if taxopark1.price > target.price:
                target = car
        return target
