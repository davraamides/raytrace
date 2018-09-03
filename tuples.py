"""
3D Tuples, Points and Vectors in homogenous coordinates
"""
import math

class Tuple(tuple):
    """All points and vectors are represented as 4D tuples with x, y, z and w coordinates.
    Points have their w coordinate set to 1.0 to indicate a position and vectors have their
    w coordinate set to 0.0 to indicate a direction.

    To keep this simple, we just alias class methods Point and Vector as initializers for
    Tuples following these conventions.
    """
    # need to use new since we are inheriting from immutable tuple
    def __new__(self, x, y, z, w):
        return tuple.__new__(Tuple, (x, y, z, w))

    @staticmethod
    def Point(x, y, z):
        return Tuple(x, y, z, 1.0)

    @staticmethod
    def Vector(x, y, z):
        return Tuple(x, y, z, 0.0)

    # special type checks because Point and Vector aren't true types
    @staticmethod
    def is_point(t):
        return isinstance(t, Tuple) and len(t) == 4 and t[3] == 1.0

    @staticmethod
    def is_vector(t):
        return isinstance(t, Tuple) and len(t) == 4 and t[3] == 0.0

    def __add__(self, other):
        return Tuple(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        return Tuple(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __neg__(self):
        return Tuple(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, other):
        return Tuple(self.x * other, self.y * other, self.z * other, self.w * other)

    def __truediv__(self, other):
        return Tuple(self.x / other, self.y / other, self.z / other, self.w / other)

    def __div__(self, other):
        return Tuple(self.x / other, self.y / other, self.z / other, self.w / other)

    def mag(self):
        return math.sqrt(sum(_ * _ for _ in self))

    def norm(self):
        return self / self.mag()

    def dot(self, other): # Jack's 914-833 3500
        return sum([a * b for a, b in zip(self, other)])

    def cross(self, other):
        # only works for vectors
        assert self.w == 0 and other.w == 0
        a, b = self, other
        return Tuple(
            a.y * b.z - a.z * b.y,
            a.z * b.x - a.x * b.z,
            a.x * b.y - a.y * b.x,
            0.0,
            )

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    @property
    def z(self):
        return self[2]

    @property
    def w(self):
        return self[3]

# create aliases so we don't need to prefix with Tuple everywhere
Point = Tuple.Point
Vector = Tuple.Vector

