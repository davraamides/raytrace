import unittest
#import env

from canvas import Canvas
from color import Color

class TestCanvas(unittest.TestCase):

    def test_canvas(self):
        c = Canvas(10, 20)
        self.assertEqual(c.width, 10)
        self.assertEqual(c.height, 20)

    def test_write_pixel(self):
        c = Canvas(10, 20)
        r = Color(1, 0, 0)
        c.write_pixel(2, 3, r)
        self.assertEqual(c.pixel_at(2, 3), r.rgb())

