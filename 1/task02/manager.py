from laptops import Laptop


class Manager:
    @staticmethod
    def find_max_price(laptops):
        if not isinstance(laptops, (list, tuple)):
            return Laptop

            target = laptops [0]

            for laptop in laptops:
                if (isinstance(laptop, Laptop):
                    if laptop.price < target.price:
                    target = laptop
            return target
