
import unittest
from datetime import datetime, timedelta

from Battery import NubbinBattery
from Battery import SpindlerBattery
from Engine import CapuletEngine
from Engine  import SternmanEngine
from Engine import WilloughbyEngine
from car import Car
from CarFactory import CarFactory


def add_years_to_date(date, years):
    try:
        return date.replace(year=date.year + years)
    except ValueError:
        return date + (datetime(date.year + years, 1, 1) - datetime(date.year, 1, 1))

# Tests for Car with WilloughbyEngine and SpindlerBattery
class TestCar(unittest.TestCase):
    def setUp(self):
        self.engine = WilloughbyEngine(61000, 29000)
        self.battery = SpindlerBattery(datetime.today() - timedelta(days=2*365), datetime.today())
        self.car = Car(self.engine, self.battery)
        
    def test_needs_service(self):
        self.assertEqual(self.car.needs_service(), True)

# Tests for CarFactory creating a calliope
class TestCarFactory(unittest.TestCase):
    def test_create_calliope(self):
        car = CarFactory.create_calliope(datetime.today(), datetime.today() - timedelta(days=2*365), 31000, 29000)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)
        self.assertEqual(car.needs_service(), True)

# Tests for CarFactory creating a glissade
class TestCarFactoryGlissade(unittest.TestCase):
    def test_create_glissade(self):
        car = CarFactory.create_glissade(datetime.today(), datetime.today() - timedelta(days=2*365), 61000, 29000)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)
        self.assertEqual(car.needs_service(), True)

# Tests for CarFactory creating a palindrome
class TestCarFactoryPalindrome(unittest.TestCase):
    def test_create_palindrome(self):
        car = CarFactory.create_palindrome(datetime.today(), datetime.today() - timedelta(days=2*365), True)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, SternmanEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)
        self.assertEqual(car.needs_service(), True)

# Tests for CarFactory creating a rorschach
class TestCarFactoryRorschach(unittest.TestCase):
    def test_create_rorschach(self):
        car = CarFactory.create_rorschach(datetime.today(), datetime.today() - timedelta(days=4*365), 61000, 29000)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, NubbinBattery)
        self.assertEqual(car.needs_service(), True)

# Tests for CarFactory creating a thovex
class TestCarFactoryThovex(unittest.TestCase):
    def test_create_thovex(self):
        car = CarFactory.create_thovex(datetime.today(), datetime.today() - timedelta(days=4*365), 31000, 29000)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, NubbinBattery)
        self.assertEqual(car.needs_service(), True)

if __name__ == '__main__':
    unittest.main()

