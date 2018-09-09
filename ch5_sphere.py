"""
"""
import math
from PIL import Image
from tuples import Point
from matrix import Matrix
from sphere import Sphere
from ray import Ray

W = 200
H = 200
D = 200
im = Image.new('RGB', (W, H))
pix = im.load()

if False:
    ## this is done in image coordinates
    eye = Point(W / 2, H / 2, D)
    sphere = Sphere()
    ts = Matrix.scale(50, 50, 50)
    tt = Matrix.translate(W / 2, H / 2, D / 4)
    sphere.transform = tt * ts

    for x in range(W):
        for y in range(H):
            ray = Ray(eye, Point(x, y, 0) - eye)
            xs = sphere.intersect(ray)
            if xs:
                pix[x, y] = (255, 0, 0)
        print(x)

else:
    ## this is done in object coordinates
    eye = Point(0, 0, -5)
    sphere = Sphere()
    tt = Matrix.translate(0, 0, -2)
    sphere.transform = tt
    wall = (-3, 3, -3, 3) # LRBT

    ms = Matrix.scale(float(wall[1] - wall[0]) / W, float(wall[3] - wall[2]) / H, 1.0)
    mt = Matrix.translate(wall[0], wall[2], 0)
    m = mt * ms


    for x in range(W):
        #xobj = float(x * (wall[1] - wall[0])) / W + wall[0]
        for y in range(H):
            #yobj = float(y * (wall[3] - wall[2])) / H + wall[2]
            p = m * Point(x, y, 0)
            ray = Ray(eye, p - eye)
            xs = sphere.intersect(ray)
            if xs:
                pix[x, y] = (255, 0, 0)
        print(x)

im.show()

