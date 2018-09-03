import math
import unittest

from matrix import Matrix
from tuples import Point, Vector

# tests for methods use for various transformations
class TestMatrixTransformations(unittest.TestCase):

    def assertTupleEqual(self, t1, t2):
        for a, b in zip(t1, t2):
            self.assertAlmostEqual(a, b, places=5)

    def assertMatrixEqual(self, m1, m2):
        self.assertEqual(m1.size, m2.size)
        for i in range(m1.size):
            for j in range(m2.size):
                self.assertAlmostEqual(m1[i, j], m2[i, j], places=5)

    def test_translation(self):
        t = Matrix.translate(5, -3, 2)
        p = Point(-3, 4, 5)
        self.assertEqual(t * p, Point(2, 1, 7))
        self.assertEqual(t.inverse() * p, Point(-8, 7, 3))
        v = Vector(-3, 4, 5)
        self.assertEqual(t * v, v)
        self.assertEqual(t.inverse() * v, v)

    def test_scaling(self):
        s = Matrix.scale(2, 3, 4)
        p = Point(-4, 6, 8)
        self.assertEqual(s * p, Point(-8, 18, 32))
        v = Vector(-4, 6, 8)
        self.assertEqual(s * v, Vector(-8, 18, 32))
        self.assertEqual(s.inverse() * v, Vector(-2, 2, 2))
        s = Matrix.scale(-1, 1, 1)
        p = Point(2, 3, 4)
        self.assertEqual(s * p, Point(-2, 3, 4))

    def test_rotation(self):
        p = Point(0, 1, 0)
        r = math.sqrt(2) / 2
        self.assertTupleEqual(Matrix.rotate_x(math.pi / 4) * p, Point(0, r, r))
        self.assertTupleEqual(Matrix.rotate_x(math.pi / 2) * p, Point(0, 0, 1))
        # NOTE: error in draft of book where he uses inverse instead of transpose
        self.assertTupleEqual(Matrix.rotate_x(math.pi / 4).transpose() * p, Point(0, r, -r))

        p = Point(0, 0, 1)
        self.assertTupleEqual(Matrix.rotate_y(math.pi / 4) * p, Point(r, 0, r))
        self.assertTupleEqual(Matrix.rotate_y(math.pi / 2) * p, Point(1, 0, 0))

        p = Point(0, 1, 0)
        self.assertTupleEqual(Matrix.rotate_z(math.pi / 4) * p, Point(-r, r, 0))
        self.assertTupleEqual(Matrix.rotate_z(math.pi / 2) * p, Point(-1, 0, 0))

    def test_shearing(self):
        p = Point(2, 3, 4)
        self.assertEqual(Matrix.shear(1, 0, 0, 0, 0, 0) * p, Point(5, 3, 4))
        self.assertEqual(Matrix.shear(0, 1, 0, 0, 0, 0) * p, Point(6, 3, 4))
        self.assertEqual(Matrix.shear(0, 0, 1, 0, 0, 0) * p, Point(2, 5, 4))
        self.assertEqual(Matrix.shear(0, 0, 0, 1, 0, 0) * p, Point(2, 7, 4))
        self.assertEqual(Matrix.shear(0, 0, 0, 0, 1, 0) * p, Point(2, 3, 6))
        self.assertEqual(Matrix.shear(0, 0, 0, 0, 0, 1) * p, Point(2, 3, 7))

    def test_combinations(self):
        p = Point(1, 0, 1)
        a = Matrix.rotate_x(math.pi / 2)
        b = Matrix.scale(5, 5, 5)
        c = Matrix.translate(10, 5, 7)

        p2 = a * p
        self.assertTupleEqual(p2, Point(1, -1, 0))
        p3 = b * p2
        self.assertTupleEqual(p3, Point(5, -5, 0))
        p4 = c * p3
        self.assertTupleEqual(p4, Point(15, 0, 7))

        self.assertTupleEqual(c * b * a * p, Point(15, 0, 7))


