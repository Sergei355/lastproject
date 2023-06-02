import unittest
from car import Cars
from minibus import Minibuses
from manager import Manager


class ManagerTest(unittest.TestCase):

    def test_cheak_min_price_taxopark(self):
        car1 = Cars("Mazda", "626", 5000, 2, 7)
        car2 = Cars("Opel", "Omega", 4000, 2.5, 8)
        car3 = Cars("Ford", "Mondeo", 3500, 1.8, 6)
        car4 = Minibuses("Ford", "Tranzit", 8000, 2.5, 9, 25)
        car5 = Minibuses("Peugeot", "Partner", 7500, 2.4, 9, 30)

        taxopark = [car1, car2, car3, car4, car5]

        expected = 3500

        actual = Manager.find_min_price_taxopark(taxopark)

        self.assertEqual(expected, actual)


    def test_cheak_max_price_taxopark_(self):
        car1 = Cars("Mazda", "626", 5000, 2, 7)
        car2 = Cars("Opel", "Omega", 4000, 2.5, 8)
        car3 = Cars("Ford", "Mondeo", 3500, 1.8, 6)
        car4 = Minibuses("Ford", "Tranzit", 8000, 2.5, 9, 25)
        car5 = Minibuses("Peugeot", "Partner", 7500, 2.4, 9, 30)

        taxopark = [car1, car2, car3, car4, car5]

        expected = 8000

        actual = Manager.find_max_price_taxopark(taxopark)

        self.assertEqual(expected, actual)

    def test_cheak_general_price_taxopark_(self):
        car1 = Cars("Mazda", "626", 5000, 2, 7)
        car2 = Cars("Opel", "Omega", 4000, 2.5, 8)
        car3 = Cars("Ford", "Mondeo", 3500, 1.8, 6)
        car4 = Minibuses("Ford", "Tranzit", 8000, 2.5, 9, 25)
        car5 = Minibuses("Peugeot", "Partner", 7500, 2.4, 9, 30)

        taxopark = [car1, car2, car3, car4, car5]

        expected = 28000

        actual = Manager.find_general_price_taxopark(taxopark)

        self.assertEqual(expected, actual)

    def test_cheak_size_car_taxopark_(self):
        car1 = Cars("Mazda", "626", 5000, 2, 7)
        car2 = Cars("Opel", "Omega", 4000, 2.5, 8)
        car3 = Cars("Ford", "Mondeo", 3500, 1.8, 6)
        car4 = Minibuses("Ford", "Tranzit", 8000, 2.5, 9, 25)
        car5 = Minibuses("Peugeot", "Partner", 7500, 2.4, 9, 30)

        taxopark1 = [car1, car2]
        taxopark2 = [car3, car4, car5]

        expected = 3

        actual = Manager.find_big_taxopark(taxopark1, taxopark2)

        self.assertEqual(expected, actual)

    def test_cheak_max_price_taxopark_with_zero(self):
        car1 = Cars("Mazda", "626", 0, 2, 7)
        car2 = Cars("Opel", "Omega", 0, 2.5, 8)
        car3 = Cars("Ford", "Mondeo", -1, 1.8, 6)
        car4 = Minibuses("Ford", "Tranzit", 0, 2.5, 9, 25)
        car5 = Minibuses("Peugeot", "Partner", -2, 2.4, 9, 30)

        taxopark = [car1, car2, car3, car4, car5]

        expected = 0

        actual = Manager.find_max_price_taxopark(taxopark)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
