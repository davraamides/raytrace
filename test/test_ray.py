import unittest

from tuples import Point, Vector
from ray import Ray

class TestRay(unittest.TestCase):

    def assertColorEqual(self, c1, c2):
        self.assertAlmostEqual(c1.r, c2.r)
        self.assertAlmostEqual(c1.g, c2.g)
        self.assertAlmostEqual(c1.b, c2.b)

    def test_create_ray(self):
        origin = Point(1, 2, 3)
        direction = Vector(4, 5, 6)
        r = Ray(origin, direction)
        self.assertEqual(r.origin, origin)
        self.assertEqual(r.direction, direction)

    def test_ray_position(self):
        r = Ray(Point(2, 3, 4), Vector(1, 0, 0))
        self.assertEqual(r.position(0.0), Point(2, 3, 4))
        self.assertEqual(r.position(1.0), Point(3, 3, 4))
        self.assertEqual(r.position(-1.0), Point(1, 3, 4))
        self.assertEqual(r.position(2.5), Point(4.5, 3, 4))