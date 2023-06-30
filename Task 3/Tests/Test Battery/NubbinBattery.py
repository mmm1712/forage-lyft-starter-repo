import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def setUp(self):
        self.battery = NubbinBattery(datetime.today() - timedelta(days=4*365), datetime.today())
        
    def test_needs_service(self):
        self.assertEqual(self.battery.needs_service(), True)

