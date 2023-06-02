import unittest
from car import Cars
from minibus import Minibuses
from manager import Manager

class ManagerTest(unittest.TestCase):

    def test_cheak_min_price_taxopark_7788(self):
        car1 = Cars("Mazda", "626", 5000, 2, 7)
        car2 = Cars("Opel", "Omega", 4000, 2.5, 8)
        car3 = Cars("Ford", "Mondeo", 3500, 1.8, 6)
        car4 = Minibuses("Ford", "Tranzit", 8000, 2.5, 9, 25)
        car5 = Minibuses("Peugeot", "Partner", 7500, 2.4, 9, 30)

        taxopark = [car1, car2, car3, car4, car5]

        expected = 3500

        actual = Manager.find_min_price_taxopark(taxopark)

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()

