import unittest

from engine.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def setUp(self):
        self.engine = WilloughbyEngine(61000, 29000)
        
    def test_needs_service(self):
        self.assertEqual(self.engine.needs_service(), True)