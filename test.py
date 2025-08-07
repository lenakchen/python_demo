import unittest
from unittest import TestCase
from platform_technical_screen import sort

class TestPackage(TestCase):

    def test_standard_output(self):
        label = sort(width=100, height=100, length=90, mass=19)
        self.assertTrue(label == "STANDARD")

    def test_large_width(self):
        label = sort(width=150, height=10, length=10, mass=10)
        self.assertTrue(label == "SPECIAL")

    def test_large_volume(self):
        label = sort(width=100, height=100, length=100, mass=10)
        self.assertTrue(label == "SPECIAL")

    def test_heavy_weight(self):
        label = sort(width=10, height=100, length=100, mass=20)
        self.assertTrue(label == "SPECIAL")

    def test_reject_output(self):
        label = sort(width=10, height=150, length=100, mass=20)
        self.assertTrue(label == "REJECTED")

if __name__ == '__main__':
    unittest.main()