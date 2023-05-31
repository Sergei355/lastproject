from car import Cars
from minibus import Minibuses
from electrocar import Electrocars
from truck import Trucks
from manager import Manager


def main():
    car1 = Cars("Mazda", "626", 5000, 2, 7)
    car2 = Cars("Opel", "Omega", 4000, 2.5, 8)
    car3 = Cars("Ford", "Mondeo", 3500, 1.8, 6)
    car4 = Minibuses("Ford", "Tranzit", 8000, 2.5, 9, 25)
    car5 = Minibuses("Peugeot", "Partner", 7500, 2.4, 9, 30)
    car6 = Electrocars("Nissan", "Leaf", 15000, 300)
    car7 = Electrocars("Tesla", "Model_3", 40000, 800)
    car8 = Trucks("Iveco", "Daily", 50000, 2.3, 11, 50)
    car9 = Trucks("Renault", "Master", 45000, 1.9, 12, 40)

    taxopark_7788 = [car1, car2, car4, car7]
    taxopark_135 = [car6, car3, car8, car9, car5]

    for car in taxopark_7788:
        print(car)

    for car in taxopark_135:
        print(car)


    max_price_1 = Manager.find_max_price_taxopark(taxopark_7788)
    min_price_1 = Manager.find_min_price_taxopark(taxopark_7788)
    max_price_2 = Manager.find_max_price_taxopark(taxopark_135)
    min_price_2 = Manager.find_min_price_taxopark(taxopark_135)
    gen_price_1 = Manager.find_general_price_taxopark(taxopark_7788)
    gen_price_2 = Manager.find_general_price_taxopark(taxopark_135)
    big_taxopark = Manager.find_big_taxopark(taxopark_135, taxopark_7788)

    print(f"The maximum price of a car in taxi depot No 7788 is = {max_price_1}." 
          f"\nThe minimum price of a car in taxi depot No. 7788 is = {min_price_1}." 
          f"\nThe maximum price of a car in taxi depot No. 135 is = {max_price_2}." 
          f"\nThe minimum price of a car in taxi depot No. 135 is = {min_price_2}."
          f"\nThe general price of a car in taxi depot No. 7788 is = {gen_price_1}."
          f"\nThe general price of a car in taxi depot No. 135 is = {gen_price_2}."
          f"\nThe largest taxi company have {big_taxopark} cars")


if __name__ == "__main__":
    main()
