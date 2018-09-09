import unittest
from tuples import Point, Vector
from matrix import Matrix
from ray import Ray
from sphere import Sphere

class TestSphere(unittest.TestCase):

    def test_intersect(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].object, s)
        self.assertEqual(xs[1].object, s)

    def test_transformation(self):
        s = Sphere()
        self.assertEqual(s.transform, Matrix.identity())

        t = Matrix.translate(2, 3, 4)
        s.transform = t
        self.assertEqual(s.transform, t)

    def test_intersect_with_transform(self):
        # intersect a scaled sphere
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        s.transform = Matrix.scale(2, 2, 2)
        xs = s.intersect(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 3)
        self.assertEqual(xs[1].t, 7)

        # intersect a translated sphere
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        s.transform = Matrix.translate(5, 0, 0)
        xs = s.intersect(r)
        self.assertEqual(len(xs), 0)
