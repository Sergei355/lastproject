from cars import Cars
from minibuses import Minibuses
from electrocars import Electrocars
from trucks import Trucks
from manager import Manager


def main():
    car1 = Cars("Mazda", "626", 5000, 2, 7)
    car2 = Cars("Opel", "omega", 4000, 2.5, 8)
    car3 = Cars("Ford", "mondeo", 3500, 1.8, 6)
    car4 = Minibuses("Ford", "tranzit", 8000, 2.5, 9, 25)
    car5 = Minibuses("Peugeot", "partner", 7500, 2.4, 9, 30)
    car6 = Electrocars("Nissan", "leaf", 15000, 300)
    car7 = Electrocars("Tesla", "model3", 40000, 800)
    car8 = Trucks("Iveco", "daily", 50000, 2.3, 11, 50)
    car9 = Trucks("Renault", "master", 45000, 1.9, 12, 40)

    taxopark1 = [car1, car2, car4, car7]
    taxopark2 = [car6, car3, car8, car9, car5]

    for car in taxopark1:
        print(car)

    for car in taxopark2:
        print(car)

    max_price = Manager.find_max_price(taxopark1)


    print(f"max price = {max_price}")




if __name__ == "__main__":
    main()
