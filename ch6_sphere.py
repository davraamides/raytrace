"""
"""
import math
from PIL import Image
from tuples import Point
from matrix import Matrix
from sphere import Sphere
from color import Color
from ray import Ray
import intersection
from light import PointLight, lighting

W = 200
H = 200
D = 200
im = Image.new('RGB', (W, H))
pix = im.load()

sphere = Sphere()
sphere.material.color = Color(1, 0.2, 1)
light_color = Color(1, 1, 1)
light_position = Point(-10, 10, -10)
light = PointLight(light_position, light_color)

## this is done in object coordinates
eye = Point(0, 0, -5)
tt = Matrix.translate(0, 0, -2)
sphere.transform = tt
wall = (-3, 3, -3, 3) # LRBT

# the -1 flips the y-coordinate so it's up
my = Matrix.scale(1.0, -1.0, 1.0)
ms = Matrix.scale(float(wall[1] - wall[0]) / W, float(wall[3] - wall[2]) / H, 1.0)
mt = Matrix.translate(wall[0], wall[2], 0)
m = my * mt * ms

_debug = False
_pause = _debug

def dprint(s):
    if _debug:
        print(s)

def pause():
    if _pause:
        s = input("Press any key...")

for x in range(W):
    for y in range(H):
        p = m * Point(x, y, 0)
        ray = Ray(eye, (p - eye).norm())
        xs = sphere.intersect(ray)
        if xs:
            dprint(f"\nSphere hit at {x}, {y}...")
            dprint("p: {}".format(p))
            dprint("ray: {}".format(ray))
            dprint("xs: {}".format(str(xs)))
            hit = intersection.hit(xs)
            dprint("hit: {}".format(hit))
            point = ray.position(hit.t)
            dprint("point: {}".format(point))
            normal = hit.object.normal(point)
            dprint("normal: {}".format(normal))
            eyev = -ray.direction
            dprint("eyev: {}".format(eyev))
            c = lighting(hit.object.material, light, point, eyev, normal, components=True)
            dprint("color: {}".format(c))
            color = c[0] + c[1] + c[2]
            pix[x, y] = color.rgb()
            pause()
    print(x)

im.show()

