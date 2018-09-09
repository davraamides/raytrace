import unittest

from tuples import Point, Vector
from matrix import Matrix
from ray import Ray
from sphere import Sphere

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

    def test_intersect_sphere(self):
        # through the center
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 4)
        self.assertEqual(xs[1].t, 6)

        # at a tangent
        r = Ray(Point(0, 1, -5), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 5)
        self.assertEqual(xs[1].t, 5) # why two points?

        # no intersection
        r = Ray(Point(0, 2, -5), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(len(xs), 0)

        # starting inside the sphere
        r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, -1)
        self.assertEqual(xs[1].t, 1)

        # starting past the sphere
        r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, -6)
        self.assertEqual(xs[1].t, -4)
       
    def test_translation(self):
        r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
        m = Matrix.translate(3, 4, 5)
        r2 = m.transform(r)
        self.assertEqual(r2.origin, Point(4, 6, 8))
        self.assertEqual(r2.direction, Vector(0, 1, 0))

    def test_scaling(self):
        r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
        m = Matrix.scale(2, 3, 4)
        r2 = m.transform(r)
        self.assertEqual(r2.origin, Point(2, 6, 12))
        self.assertEqual(r2.direction, Vector(0, 3, 0))


