import unittest
from intersection import Intersection, hit
from sphere import Sphere

class TestIntersection(unittest.TestCase):

    def test_create(self):
        s = Sphere()
        i = Intersection(3.5, s)
        self.assertEqual(i.t, 3.5)
        self.assertEqual(i.object, s)

    def test_list(self):
        s = Sphere()
        xs = (Intersection(1, s), Intersection(2, s))
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 1)
        self.assertEqual(xs[1].t, 2)

    def test_hit(self):
        # test hit with positive t
        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = (i1, i2)
        h = hit(xs)
        self.assertEqual(h, i1)

        # test hit with some negative t intersections
        i1 = Intersection(-1, s)
        i2 = Intersection(1, s)
        xs = (i1, i2)
        h = hit(xs)
        self.assertEqual(h, i2)

        # test hit with all negative t intersections
        i1 = Intersection(-2, s)
        i2 = Intersection(-1, s)
        xs = (i1, i2)
        h = hit(xs)
        self.assertIsNone(h)

        # test hit is lowest non-negative t value
        i1 = Intersection(5, s)
        i2 = Intersection(7, s)
        i3 = Intersection(-3, s)
        i4 = Intersection(2, s)
        xs = (i1, i2, i3, i4)
        h = hit(xs)
        self.assertEqual(h, i4)

