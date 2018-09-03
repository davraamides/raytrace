"""
"""
import math
from PIL import Image
from tuples import Point
from matrix import Matrix

S = 500
im = Image.new('RGB', (S, S))
pix = im.load()

d = int(S * 0.4) # the length of the "hand" is a little less than half the canvas size
p = Point(0, 1, 0) # assume canvas is in XY plane so this is the 12 o'clock position

for i in range(12):
    r = Matrix.rotate_z(i * math.pi / 6) # 2pi/12 positions or pi/6
    q = r * p
    q = Matrix.scale(d, d, 0) * q # make it the size of the "hand" dimensions
    q = Matrix.translate(S/2, S/2, 0) * q # move to the origin of the canvas, really could do S/2, -S/2
    pix[int(q.x), S - int(q.y)] = (255, 255, 255)
    print("{}, {}".format(int(q.x), S - int(q.y)))
im.show()

