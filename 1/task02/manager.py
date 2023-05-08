from laptops import Laptop


class Manager:
    @staticmethod
    def find_max_price(laptops):
        if isinstance(laptops, (list, tuple)):
            count = 0

            for laptop in laptops:
                if (isinstance(laptop, Laptop)
                        and laptop.price > laptop.price + 1):
                    return count
