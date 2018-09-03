"""
RGB color
"""
class Color(tuple):
    # need to use new since we are inheriting from immutable tuple
    def __new__(self, r, g, b):
        return tuple.__new__(Color, (r, g, b))

    @property
    def r(self):
        return self[0]

    @property
    def g(self):
        return self[1]

    @property
    def b(self):
        return self[2]

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __sub__(self, other):
        return Color(self.r - other.r, self.g - other.g, self.b - other.b)

    def __mul__(self, other):
        if isinstance(other, Color):
            return Color(self.r * other.r, self.g * other.g, self.b * other.b)
        else:
            return Color(self.r * other, self.g * other, self.b * other)

    def rgb(self, minval=0, maxval=255):
        """Assumes Color is in 0.0 to 1.0 range
        """
        def clamp(x):
            return min(max(minval, x), maxval)

        return tuple([clamp(int(_ * (maxval - minval)) + minval) for _ in self])

