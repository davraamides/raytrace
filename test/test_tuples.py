import unittest
import math
from tuples import Point, Vector, Tuple

class TestTuple(unittest.TestCase):

    def test_point(self):
        p = Point(4.3, -4.2, 3.1)
        self.assertEqual(p.x, 4.3)
        self.assertEqual(p.y, -4.2)
        self.assertEqual(p.z, 3.1)
        self.assertEqual(p.w, 1.0)

    def test_vector(self):
        v = Vector(4.3, -4.2, 3.1)
        self.assertEqual(v.x, 4.3)
        self.assertEqual(v.y, -4.2)
        self.assertEqual(v.z, 3.1)
        self.assertEqual(v.w, 0.0)

    def test_point_tuple_equality(self):
        p = Point(4, -4, 3)
        t = Tuple(4, -4, 3, 1)
        self.assertEqual(p, t)

    def test_vector_tuple_equality(self):
        a = Vector(4, -4, 3)
        t = Tuple(4, -4, 3, 0)
        self.assertEqual(a, t)

    def test_addition(self):
        t1 = Tuple(3, -2, 5, 1)
        t2 = Tuple(-2, 3, 1, 0)
        self.assertEqual(t1 + t2, Tuple(1, 1, 6, 1))

    def test_subtraction(self):
        t1 = Tuple(3, -2, 5, 1)
        t2 = Tuple(-2, 3, 1, 0)
        self.assertEqual(t1 - t2, Tuple(5, -5, 4, 1))

    def test_point_subtraction(self):
        # subtracting two points results in a vector
        p1 = Point(3, 2, 1)
        p2 = Point(5, 6, 7)
        self.assertEqual(p1 - p2, Vector(-2, -4, -6))

        # subtracting a vector from a point results in a new point
        p = Point(3, 2, 1)
        v = Vector(5, 6, 7)
        self.assertEqual(p - v, Point(-2, -4, -6))

    def test_vector_subtraction(self):
        # subtracting two vectors results in a vector
        v1 = Vector(3, 2, 1)
        v2 = Vector(5, 6, 7)
        self.assertEqual(v1 - v2, Vector(-2, -4, -6))

    def test_negation(self):
        a = Tuple(1, -2, 3, -4)
        self.assertEqual(-a, Tuple(-1, 2, -3, 4))

    def test_scalar_multiplication(self):
        a = Tuple(1, -2, 3, -4)
        self.assertEqual(a * 3.5, Tuple(3.5, -7, 10.5, -14))
        self.assertEqual(a * 0.5, Tuple(0.5, -1, 1.5, -2))

    def test_scalar_division(self):
        a = Tuple(1, -2, 3, -4)
        self.assertEqual(a / 2.0, Tuple(0.5, -1, 1.5, -2))

    def test_magnitude(self):
        self.assertEqual(1, Vector(1, 0, 0).mag())
        self.assertEqual(1, Vector(0, 1, 0).mag())
        self.assertEqual(1, Vector(0, 0, 1).mag())
        self.assertEqual(math.sqrt(14), Vector(1, 2, 3).mag())
        self.assertEqual(math.sqrt(14), Vector(-1, -2, -3).mag())

    def test_normalization(self):
        self.assertEqual(Vector(1, 0, 0), Vector(4, 0, 0).norm())
        x = math.sqrt(14)
        self.assertEqual(Vector(1 / x, 2 / x, 3 / x), Vector(1, 2, 3).norm())
        # the magnitude of a normalized vector should always be 1.0
        self.assertEqual(1, Vector(1, 2, 3).norm().mag())

    def test_dot_product(self):
        a = Vector(1, 2, 3)
        b = Vector(2, 3, 4)
        self.assertEqual(20, a.dot(b))

    def test_cross_product(self):
        a = Vector(1, 2, 3)
        b = Vector(2, 3, 4)
        self.assertEqual(Vector(-1, 2, -1), a.cross(b))
        self.assertEqual(Vector(1, -2, 1), b.cross(a))

if __name__ == '__main__':
    unittest.main()