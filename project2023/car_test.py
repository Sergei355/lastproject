import unittest
from car import Cars


class CarTest(unittest.TestCase):

    def test_price_property_positive(self):
        cars = Cars()
        expected = 1
        cars.price = 1
        self.assertEqual(expected, cars.price)

    def test_price_property_with_zero(self):
        cars = Cars()
        expected = 0
        cars.price = 0
        self.assertEqual(expected, cars.price)

    def test_price_property_negative(self):
        cars = Cars()
        expected = cars.price
        cars.price = -1
        self.assertEqual(expected, cars.price)

    def test_car_default_constructor(self):
        cars = Cars()
        expected_price = 1
        expected_model = "no name"
        expected_brand = "no name"
        expected_engine_capacity = 2
        expected_fuel_consumption = 5
        self.assertEqual(expected_price, cars.price)
        self.assertEqual(expected_model, cars.model)
        self.assertEqual(expected_brand, cars.brand)
        self.assertEqual(expected_engine_capacity, cars.engine_capacity)
        self.assertEqual(expected_fuel_consumption, cars.fuel_consumption)

    def test_car_constructor_with_args(self):
        expected_price = 100
        expected_model = "Alex"
        expected_brand = "VicVic"
        expected_engine_capacity = 5
        expected_fuel_consumption = 8

        cars = Cars(expected_price, expected_model, expected_brand, expected_engine_capacity,
                        expected_fuel_consumption)

        self.assertEqual(expected_price, cars.price)
        self.assertEqual(expected_model, cars.model)
        self.assertEqual(expected_brand, cars.brand)
        self.assertEqual(expected_engine_capacity, cars.engine_capacity)
        self.assertEqual(expected_fuel_consumption, cars.fuel_consumption)


if __name__ == "__main__":
    unittest.main()
