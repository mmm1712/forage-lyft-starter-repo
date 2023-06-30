import unittest
from datetime import date, timedelta
from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def setUp(self):
        last_service_date = date.today() - timedelta(days=4*365)
        current_date = date.today()
        self.battery = NubbinBattery(last_service_date, current_date)

    def test_needs_service(self):
        self.assertEqual(self.battery.needs_service(), True)

