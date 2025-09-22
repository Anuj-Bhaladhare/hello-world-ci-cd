import unittest
from app import App

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App("TestApp")

    def test_greet(self):
        self.assertEqual(self.app.greet(), "Hello, Python Programming!")

# this is the comment        