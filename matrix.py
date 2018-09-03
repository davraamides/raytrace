"""
A square matrix for 3D geometric manipulations
"""
import copy
import math

from tuples import Tuple

class Matrix(object):
    def __init__(self, size=4, vals=None):
        if vals:
            self.m = copy.deepcopy(vals)
        else:
            self.m = self._create(size)

    @staticmethod
    def identity(size=4):
        m = Matrix(size=size)
        for i in range(size):
            m.m[i][i] = 1.0
        return m

    @property
    def size(self):
        return len(self.m)

    def __getitem__(self, key):
        """Suppport indexing as [x, y] by treating key as a tuple
        """
        return self.m[key[0]][key[1]]

    def __repr__(self):
        s = []
        for i in range(self.size):
            s.append("[{}]".format(', '.join("{}".format(_) for _ in self.m[i])))
        return "[" + '\n'.join(s) + "]"

    def __eq__(self, other):
        return self.size == other.size and self.m == other.m

    def __mul__(self, other):
        if isinstance(other, Matrix):
            a, b = self, other
            assert a.size == b.size
            m = self._create(a.size)
            for r in range(a.size):
                for c in range(a.size):
                    m[r][c] = sum(a[r, i] * b[i, c] for i in range(a.size))
            return Matrix(vals=m)
        if isinstance(other, Tuple):
            a, b = self, other
            assert a.size == len(b)
            t = [0.0] * a.size
            for r in range(a.size):
                    t[r] = sum(a[r, i] * b[i] for i in range(a.size))
            return Tuple(*t)

    def transpose(self):
        m = self._create(self.size)
        for i in range(self.size):
            for j in range(self.size):
                m[i][j] = self.m[j][i]
        return Matrix(vals=m)

    def inverse(self):
        d = self._determinant()
        if not d:
            raise ValueError("Matrix determinant cannot be zero")
        cf = self._create(self.size)
        for r in range(self.size):
            for c in range(self.size):
                cf[r][c] = float(self._cofactor(r, c)) / d
        return Matrix(vals=cf).transpose()

    @staticmethod
    def translate(x, y, z):
        m = Matrix.identity()
        m.m[0][3] = x
        m.m[1][3] = y
        m.m[2][3] = z
        return m

    @staticmethod
    def scale(x, y, z):
        m = Matrix.identity()
        m.m[0][0] = x
        m.m[1][1] = y
        m.m[2][2] = z
        return m

    @staticmethod
    def rotate_x(r):
        m = Matrix.identity()
        m.m[1][1] = math.cos(r)
        m.m[1][2] = -math.sin(r)
        m.m[2][1] = math.sin(r)
        m.m[2][2] = -math.cos(r)
        return m

    @staticmethod
    def rotate_y(r):
        m = Matrix.identity()
        m.m[0][0] = math.cos(r)
        m.m[0][2] = math.sin(r)
        m.m[2][0] = -math.sin(r)
        m.m[2][2] = math.cos(r)
        return m

    @staticmethod
    def rotate_z(r):
        m = Matrix.identity()
        m.m[0][0] = math.cos(r)
        m.m[0][1] = -math.sin(r)
        m.m[1][0] = math.sin(r)
        m.m[1][1] = math.cos(r)
        return m

    @staticmethod
    def shear(xy, xz, yx, yz, zx, zy):
        m = Matrix.identity()
        m.m[0][1] = xy
        m.m[0][2] = xz
        m.m[1][0] = yx
        m.m[1][2] = yz
        m.m[2][0] = zx
        m.m[2][1] = zy
        return m

    # helpers

    def _create(self, size):
        return [[0.0] * size for i in range(size)]

    def _determinant(self):
        if self.size == 2:
            return self[0, 0] * self[1, 1] - self[0, 1] * self[1, 0]
        return sum(self[0, c] * self._cofactor(0, c) for c in range(self.size))

    def _submatrix(self, r, c):
        assert self.size in (3, 4)
        m = [[self.m[i][j] for j in range(self.size) if j != c] for i in range(self.size) if i != r]
        return Matrix(vals=m)

    def _minor(self, r, c):
        return self._submatrix(r, c)._determinant()

    def _cofactor(self, r, c):
        sign = -1 if (r + c) % 2 == 1 else 1
        return sign * self._minor(r, c)

