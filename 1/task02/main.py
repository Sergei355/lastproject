from laptops import Laptop
from manager import Manager


def main():
    laptop1 = Laptop("Toshiba", "45KM0445566", 540)
    laptop2 = Laptop("ACER", "500100KLV0", 650)
    laptop3 = Laptop("DELL", "8931234KKL", 700)
    laptop4 = Laptop("Apple", "Macbook", 1000)
    laptop5 = Laptop("Lenovo", "MSQ100500", 350)

    laptops = [laptop1, laptop2, laptop3, laptop4, laptop5]

    for laptop in laptops:
        print(laptop)



    max_price = Manager.find_max_price(laptops)
    min_price = Manager.find_min_price(laptops)

    print(f"max price = {max_price}")
    print(f"min price = {min_price}")





if __name__ == "__main__":
    main()