import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def setUp(self):
        self.battery = SpindlerBattery(datetime.today() - timedelta(days=2*365), datetime.today())
        
    def test_needs_service(self):
        self.assertEqual(self.battery.needs_service(), True)
