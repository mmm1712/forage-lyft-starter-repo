import unittest
from datetime import date, timedelta


from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def setUp(self):
        last_service_date = date.today() - timedelta(days=4*365)
        current_date = date.today()
        self.battery = SpindlerBattery(last_service_date, current_date)

    def test_needs_service(self):
        self.assertEqual(self.battery.needs_service(), True)
