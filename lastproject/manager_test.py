import unittest
from manager import Manager

class Manager(unittest.TestCase):
    def test_cheak_min_price_taxopark_7788(self):
        min_price = price
        expected = 4000

        actual = Manager.find_min_price_taxopark()

        self.assertEqual(expected, actual)