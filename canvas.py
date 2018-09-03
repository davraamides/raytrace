"""
Drawing canvas using Pillow
"""
from PIL import Image
from color import Color

class Canvas(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new('RGB', (self.width, self.height))
        self.pixels = self.image.load()

    def write_pixel(self, x, y, c):
        self.pixels[x, y] = c.rgb()

    def pixel_at(self, x, y):
        return self.pixels[x, y]

    def show(self):
        self.image.show()


