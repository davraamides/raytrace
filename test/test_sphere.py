import unittest
import math
from tuples import Point, Vector
from matrix import Matrix
from ray import Ray
from sphere import Sphere
from material import Material

class TestSphere(unittest.TestCase):

    def assertTupleEqual(self, t1, t2):
        for a, b in zip(t1, t2):
            self.assertAlmostEqual(a, b, places=5)

    def test_defaults(self):
        s = Sphere()
        self.assertEqual(s.material, Material())

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

    def test_normal(self):
        s = Sphere()

        n = s.normal(Point(1, 0, 0))
        self.assertEqual(n, Vector(1, 0, 0))
        n = s.normal(Point(0, 1, 0))
        self.assertEqual(n, Vector(0, 1, 0))
        n = s.normal(Point(0, 0, 1))
        self.assertEqual(n, Vector(0, 0, 1))
        r = math.sqrt(3) / 3
        n = s.normal(Point(r, r, r))
        self.assertEqual(n, Vector(r, r, r))
        self.assertEqual(n, n.norm())

    def test_normal_with_transform(self):
        s = Sphere()
        s.transform = Matrix.translate(0, 5, 0)
        n = s.normal(Point(1, 5, 0))
        self.assertEqual(n, Vector(1, 0, 0))

        s = Sphere()
        s.transform = Matrix.scale(1, 0.5, 1)
        r = math.sqrt(2) / 2
        n = s.normal(Point(0, r, -r))
        self.assertTupleEqual(n, Vector(0, 0.97014, -0.24254))

