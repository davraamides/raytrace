import math
from tuples import Point
from matrix import Matrix
from intersection import Intersection

class Sphere(object):
    def __init__(self, radius=1):
        self.radius = radius
        self.center = Point(0, 0, 0)
        self.transform = Matrix.identity()

    def __repr__(self):
        return 'sphere(center:{}, radius:{})'.format(self.center, self.radius)

    def intersect(self, ray):
        # transform the ray back to the sphere's object space by using the inverse of its transform matrix
        ray = self.transform.inverse().transform(ray)
        sphere_to_ray = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2 * ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - self.radius ** 2
        #print(f's2r: {sphere_to_ray}')
        #print(f'ray: {ray}, sphere: {self}')
        #print(f'a: {a}, b: {b}, c: {c}')

        d = b * b - 4 * a * c
        #print(f'd: {d}')

        # test if no intersection
        if d < 0:
            return tuple()

        t1 = (-b - math.sqrt(d)) / (2 * a)
        t2 = (-b + math.sqrt(d)) / (2 * a)
        #print(f't1: {t1}, t2: {t2}')

        if t1 > t2:
            t1, t2 = t2, t1
        return (Intersection(t1, self), Intersection(t2, self))