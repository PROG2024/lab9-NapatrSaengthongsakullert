"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest

from circle import Circle


# TODO write 3 tests as described above
class CircleTest(unittest.TestCase):

    def setUp(self):
        self.circle1 = Circle(3)
        self.circle2 = Circle(4)

    def test_add_area_typical_case(self):
        self.circle3 = self.circle1.add_area(self.circle2)
        self.assertEqual(self.circle3.get_radius(), 5.0)

    def test_add_area_edge_case(self):
        self.circle4 = Circle(0)
        self.circle5 = self.circle1.add_area(self.circle4)
        self.assertEqual(self.circle5.get_radius(), self.circle1.get_radius())

    def test_negative_radius_raises_value_error(self):
        with self.assertRaises(ValueError):
            Circle(-5)
