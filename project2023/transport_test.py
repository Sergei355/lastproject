import unittest
from transport import Transport


class transportTest(unittest.TestCase):

    def test_price_property_positive(self):
        transport = Transport()
        expected = 1
        transport.price = 1
        self.assertEqual(expected, transport.price)


    def test_price_property_negative(self):
        transport = Transport()
        expected = -1
        transport.price = -1
        self.assertEqual(expected, transport.price)

    def test_price_property_with_zero(self):
        transport = Transport()
        expected = 0
        transport.price = 0
        self.assertEqual(expected, transport.price)

    def test_car_default_constructor(self):
        transport = Transport()
        expected_price = 1
        expected_model = "no name"
        expected_brand = "no name"
        self.assertEqual(expected_price, transport.price)
        self.assertEqual(expected_model, transport.model)
        self.assertEqual(expected_brand, transport.brand)






if __name__ == "__main__":
    unittest.main()
