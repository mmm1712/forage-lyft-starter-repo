import unittest

from engine.capulet_engine import CapuletEngine

# Tests for CapuletEngine
class TestCapuletEngine(unittest.TestCase):
    def setUp(self):
        self.engine = CapuletEngine(31000, 29000)
        
    def test_needs_service(self):
        self.assertEqual(self.engine.needs_service(), True)
