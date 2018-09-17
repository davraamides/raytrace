import unittest

from tuples import Point
from color import Color
from light import PointLight

class TestLight(unittest.TestCase):

    def assertColorEqual(self, c1, c2):
        self.assertAlmostEqual(c1.r, c2.r)
        self.assertAlmostEqual(c1.g, c2.g)
        self.assertAlmostEqual(c1.b, c2.b)

    def test_point_light(self):
        p = Point(0, 0, 0)
        c = Color(1, 1, 1)
        l = PointLight(p, c)
        self.assertEqual(l.position, p)
        self.assertEqual(l.intensity, c)


