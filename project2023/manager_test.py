import unittest
from car import Cars
from minibus import Minibuses
from manager import Manager


class ManagerTest(unittest.TestCase):

    def setUp(self):
        car1 = Cars("Mazda", "626", 5000, 2, 7)
        car2 = Cars("Opel", "Omega", 4000, 2.5, 8)
        car3 = Cars("Ford", "Mondeo", 3500, 1.8, 6)
        car4 = Minibuses("Ford", "Tranzit", 8000, 2.5, 9, 25)
        car5 = Minibuses("Peugeot", "Partner", 7500, 2.4, 9, 30)

        self.taxopark = [car1, car2, car3, car4, car5]

    def tearDown(self):
        del self.taxopark

    def test_cheak_min_price_taxopark(self):
        expected = 3500
        actual = Manager.find_min_price_taxopark(self.taxopark)
        self.assertEqual(expected, actual)


    def test_cheak_max_price_taxopark_(self):
        expected = 8000
        actual = Manager.find_max_price_taxopark(self.taxopark)
        self.assertEqual(expected, actual)

    def test_cheak_general_price_taxopark_(self):
        expected = 28000
        actual = Manager.find_general_price_taxopark(self.taxopark)
        self.assertEqual(expected, actual)

    def test_cheak_size_car_taxopark_(self):
        taxopark1 = self.taxopark[:2]
        taxopark2 = self.taxopark[2:]
        expected = 3
        actual = Manager.find_big_taxopark(taxopark1, taxopark2)
        self.assertEqual(expected, actual)

    def test_cheak_max_price_taxopark_with_zero(self):
        car1 = Cars("Mazda", "626", 0, 2, 7)
        car2 = Cars("Opel", "Omega", 0, 2.5, 8)
        car3 = Cars("Ford", "Mondeo", 0, 1.8, 6)
        car4 = Minibuses("Ford", "Tranzit", 0, 2.5, 9, 25)
        car5 = Minibuses("Peugeot", "Partner", 0, 2.4, 9, 30)

        taxopark = [car1, car2, car3, car4, car5]
        expected = 0
        actual = Manager.find_max_price_taxopark(taxopark)
        self.assertEqual(expected, actual)

    def test_cheak_max_price_taxopark_with_empty_list(self):
        car1 = Cars("Mazda", "626", 0, 2, 7)
        car2 = Cars("Opel", "Omega", 0, 2.5, 8)
        car3 = Cars("Ford", "Mondeo", 0, 1.8, 6)
        car4 = Minibuses("Ford", "Tranzit", 0, 2.5, 9, 25)
        car5 = Minibuses("Peugeot", "Partner", 0, 2.4, 9, 30)

        taxopark = []
        expected = 0
        actual = Manager.find_max_price_taxopark(taxopark)
        self.assertEqual(expected, actual)


    def test_cheak_max_price_taxopark_with_another_element(self):
        car1 = Cars("Mazda", "626", 5000, 2, 7)
        car2 = Cars("Opel", "Omega", 4000, 2.5, 8)
        car3 = Cars("Ford", "Mondeo", 2500, 1.8, 6)
        car4 = Minibuses("Ford", "Tranzit", 1500, 2.5, 9, 25)
        car5 = Minibuses("Peugeot", "Partner", 6000, 2.4, 9, 30)

        taxopark = [car1, car3, car2, "www",  car5]
        expected = 6000
        actual = Manager.find_max_price_taxopark(taxopark)
        self.assertEqual(expected, actual)

    def test_cheak_max_price_taxopark_with_one_element(self):
        car1 = Cars("Mazda", "626", 5000, 2, 7)
        car2 = Cars("Opel", "Omega", 4000, 2.5, 8)
        car3 = Cars("Ford", "Mondeo", 2500, 1.8, 6)
        car4 = Minibuses("Ford", "Tranzit", 1500, 2.5, 9, 25)
        car5 = Minibuses("Peugeot", "Partner", 6000, 2.4, 9, 30)

        taxopark = [car1]
        expected = 5000
        actual = Manager.find_max_price_taxopark(taxopark)
        self.assertEqual(expected, actual)

    def test_cheak_max_price_taxopark_with_diffrent_element(self):
        car1 = Cars("Mazda", "626", 5000, 2, 7)
        car2 = Cars("Opel", "Omega", 4000, 2.5, 8)
        car3 = Cars("Ford", "Mondeo", 2500, 1.8, 6)
        car4 = Minibuses("Ford", "Tranzit", 1500, 2.5, 9, 25)
        car5 = Minibuses("Peugeot", "Partner", 6000, 2.4, 9, 30)

        taxopark = [car1, "www"]
        expected = 5000
        actual = Manager.find_max_price_taxopark(taxopark)
        self.assertEqual(expected, actual)





if __name__ == "__main__":
    unittest.main()
