import unittest

from color import Color

class TestColor(unittest.TestCase):

    def assertColorEqual(self, c1, c2):
        self.assertAlmostEqual(c1.r, c2.r)
        self.assertAlmostEqual(c1.g, c2.g)
        self.assertAlmostEqual(c1.b, c2.b)

    def test_color(self):
        c = Color(-0.5, 0.4, 1.7)
        self.assertAlmostEqual(c.r, -0.5)
        self.assertAlmostEqual(c.g, 0.4)
        self.assertAlmostEqual(c.b, 1.7)

    def test_addition(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        self.assertColorEqual(c1 + c2, Color(1.6, 0.7, 1.0))

    def test_subtraction(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        self.assertColorEqual(c1 - c2, Color(0.2, 0.5, 0.5))

    def test_multiplication(self):
        # by a scalar
        c = Color(0.2, 0.3, 0.4)
        self.assertColorEqual(c * 2, Color(0.4, 0.6, 0.8))

        # by another color
        c1 = Color(1, 0.2, 0.4)
        c2 = Color(0.9, 1, 0.1)
        self.assertColorEqual(c1 * c2, Color(0.9, 0.2, 0.04))

    def test_rgb(self):
        c = Color(1, 0, 0)
        self.assertEqual(c.rgb(), (255, 0, 0))
        c = Color(0.5, 0.1, 0.3)
        self.assertEqual(c.rgb(), (127, 25, 76))
        c = Color(0, -0.1, 0)
        self.assertEqual(c.rgb(), (0, 0, 0))
        c = Color(0, 0, 1.1)
        self.assertEqual(c.rgb(), (0, 0, 255))

