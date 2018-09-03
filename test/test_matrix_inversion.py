import unittest

from matrix import Matrix

# tests for methods use for inversion
class TestMatrixInversion(unittest.TestCase):

    def assertMatrixEqual(self, m1, m2):
        self.assertEqual(m1.size, m2.size)
        for i in range(m1.size):
            for j in range(m2.size):
                self.assertAlmostEqual(m1[i, j], m2[i, j], places=5)

    def test_determinant_2x2(self):
        m = Matrix(vals=[[1, 5], [-3, 2]])
        self.assertEqual(m._determinant(), 17)

    def test_submatrix(self):
        m = Matrix(vals=[
            [1, 5, 0],
            [-3, 2, 7],
            [0, 6, -3]])
        self.assertEqual(m._submatrix(0, 2), Matrix(vals=[[-3, 2], [0, 6]]))
        m = Matrix(vals=[
            [-6, 1, 1, 6],
            [-8, 5, 8, 6],
            [-1, 0, 8, 2],
            [-7, 1, -1, 1]])
        self.assertEqual(m._submatrix(2, 1), Matrix(vals=[[-6, 1, 6], [-8, 8, 6], [-7, -1, 1]]))

    def test_minor(self):
        m = Matrix(vals=[
            [3, 5, 0],
            [2, -1, -7],
            [6, -1, 5]])
        self.assertEqual(m._minor(1, 0), 25)

    def test_cofactor(self):
        m = Matrix(vals=[
            [3, 5, 0],
            [2, -1, -7],
            [6, -1, 5]])
        self.assertEqual(m._minor(0, 0), -12)
        self.assertEqual(m._cofactor(0, 0), -12)
        self.assertEqual(m._minor(1, 0), 25)
        self.assertEqual(m._cofactor(1, 0), -25)

    def test_determinant_3x3(self):
        m = Matrix(vals=[
            [1, 2, 6],
            [-5, 8, -4],
            [2, 6, 4]])
        self.assertEqual(m._determinant(), -196)
        
    def test_determinant_4x4(self):
        m = Matrix(vals=[
            [-2, -8, 3, 5],
            [-3, 1, 7, 3],
            [1, 2, -9, 6],
            [-6, 7, 7, -9]])
        self.assertEqual(m._determinant(), -4071)

    def test_inversion(self):
        m = Matrix(vals=[
            [6, 4, 4, 4],
            [5, 5, 7, 6],
            [4, -9, 3, -7],
            [9, 1, 7, -6],
            ])
        self.assertEqual(m._determinant(), -2120)

        # verify exception if determinant is zero
        m = Matrix(vals=[
            [-4, 2, -2, -3],
            [9, 6, 2, 6],
            [0, -5, 1, -5],
            [0, 0, 0, 0]
            ])
        self.assertEqual(m._determinant(), 0)
        with self.assertRaises(ValueError):
            m.inverse()

        m = Matrix(vals=[
            [-5, 2, 6, -8],
            [1, -5, 1, 8],
            [7, 7, -6, -7],
            [1, -3, 7, 4],
            ])
        self.assertMatrixEqual(m.inverse(), Matrix(vals=[
            [0.21805, 0.45113, 0.24060, -0.04511],
            [-0.80827, -1.45677, -0.44361, 0.52068],
            [-0.07895, -0.22368, -0.05263, 0.19737],
            [-0.52256, -0.81391, -0.30075, 0.30639]
            ]))

        m = Matrix(vals=[
            [8, -5, 9, 2],
            [7, 5, 6, 1],
            [-6, 0, 9, 6],
            [-3, 0, -9, -4]])
        self.assertMatrixEqual(m.inverse(), Matrix(vals=[
            [-0.15385, -0.15385, -0.28205, -0.53846],
            [-0.07692, 0.12308, 0.02564, 0.03077],
            [0.35897, 0.35897, 0.43590, 0.92308],
            [-0.69231, -0.69231, -0.76923, -1.92308]
            ]))

        m = Matrix(vals=[
            [9, 3, 0, 9],
            [-5, -2, -6, -3],
            [-4, 9, 6, 4],
            [-7, 6, 6, 2]
            ])
        self.assertMatrixEqual(m.inverse(), Matrix(vals=[
            [-0.04074, -0.07778, 0.14444, -0.22222],
            [-0.07778, 0.03333, 0.36667, -0.33333],
            [-0.02901, -0.14630, -0.10926, 0.12963],
            [0.17778, 0.06667, -0.26667, 0.33333]
            ]))

        a = Matrix(vals=[
            [3, -9, 7, 3],
            [3, -8, 2, -9],
            [-4, 4, 4, 1],
            [-6, 5, -1, 1]
            ])
        b = Matrix(vals=[
            [8, 2, 2, 2],
            [3, -1, 7, 0],
            [7, 0, 5, 4],
            [6, -2, 0, 5]
            ])
        c = a * b
        self.assertMatrixEqual(c * b.inverse(), a)

