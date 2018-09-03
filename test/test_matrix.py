import unittest

from matrix import Matrix
from tuples import Tuple

# basic Matrix tests
class TestMatrix(unittest.TestCase):

    def test_matrix(self):
        m = Matrix()
        self.assertEqual(m[0, 0], 0.0)
        self.assertEqual(m[3, 3], 0.0)
        m = Matrix(vals=[[1, 2, 3, 4], [5.5, 6.5, 7.5, 8.5], [9, 10, 11, 12], [13.5, 14.5, 15.5, 16.5]])
        self.assertEqual(m[0, 0], 1)
        self.assertEqual(m[0, 3], 4)
        self.assertEqual(m[1, 0], 5.5)
        self.assertEqual(m[1, 2], 7.5)
        self.assertEqual(m[2, 2], 11)
        self.assertEqual(m[3, 0], 13.5)
        self.assertEqual(m[3, 2], 15.5)

    def test_matrix_size(self):
        m4 = Matrix()
        self.assertEqual(m4.size, 4)
        m3 = Matrix(size=3)
        self.assertEqual(m3.size, 3)
        m2 = Matrix(size=2)
        self.assertEqual(m2.size, 2)

    def test_matrix_multiplication(self):
        a = Matrix(vals=[
            [1, 2, 3, 4],
            [2, 3, 4, 5],
            [3, 4, 5, 6],
            [4, 5, 6, 7]])
        b = Matrix(vals=[
            [0, 1, 2, 4],
            [1, 2, 4, 8],
            [2, 4, 8, 16],
            [4, 8, 16, 32]])
        c = a * b
        self.assertEqual(c, Matrix(vals=[
            [24, 49, 98, 196],
            [31, 64, 128, 256],
            [38, 79, 158, 316],
            [45, 94, 188, 376]]))

    def test_tuple_multiplication(self):
        m = Matrix(vals=[
            [1, 2, 3, 4],
            [2, 4, 4, 2],
            [8, 6, 4, 1],
            [0, 0, 0, 1]])
        t = Tuple(1, 2, 3, 1)
        c = m * t
        self.assertEqual(c, Tuple(18, 24, 33, 1))

    def test_identity(self):
        m = Matrix(vals=[
            [0, 1, 2, 4],
            [1, 2, 4, 8],
            [2, 4, 8, 16],
            [4, 8, 16, 32]])
        i = Matrix.identity()
        self.assertEqual(1.0, i[0, 0])
        self.assertEqual(1.0, i[1, 1])
        self.assertEqual(1.0, i[2, 2])
        self.assertEqual(1.0, i[3, 3])
        self.assertEqual(m * i, m)

        t = Tuple(1, 2, 3, 4)
        self.assertEqual(i * t, t)

    def test_transpose(self):
        m = Matrix(vals=[
            [0, 9, 3, 0],
            [9, 8, 0, 8],
            [1, 8, 5, 3],
            [0, 0, 5, 8]])
        t = Matrix(vals=[
            [0, 9, 1, 0],
            [9, 8, 8, 0],
            [3, 0, 5, 5],
            [0, 8, 3, 8]])
        self.assertEqual(m.transpose(), t)
        self.assertEqual(m.transpose().transpose(), m)
        self.assertEqual(Matrix.identity().transpose(), Matrix.identity())

