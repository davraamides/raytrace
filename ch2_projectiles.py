"""
"""
from PIL import Image
from tuples import Point, Vector, Tuple

class Projectile(object):
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def __str__(self):
        return "P={}, V={}".format(self.position, self.velocity)

class World(object):
    def __init__(self, gravity, wind):
        self.gravity = gravity
        self.wind = wind

def tick(world, projectile):
    p = projectile.position + projectile.velocity
    v = projectile.velocity + world.gravity + world.wind
    return Projectile(p, v)


W, H = 900, 550
im = Image.new('RGB', (W, H))
pix = im.load()

p = Projectile(Point(0, 1, 0), Vector(1, 1.8, 0).norm() * 11.25)
w = World(Vector(0, -0.1, 0), Vector(-0.01, 0, 0))

while p.position.y > 0:
    pix[int(p.position.x), H - int(p.position.y)] = (255, 0, 0)
    print(p)
    p = tick(w, p)

im.show()

