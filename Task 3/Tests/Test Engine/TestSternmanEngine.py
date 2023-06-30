import unittest
from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def setUp(self):
        self.engine = SternmanEngine(True)
        
    def test_needs_service(self):
        self.assertEqual(self.engine.needs_service(), True)
