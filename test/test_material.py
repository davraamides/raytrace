import unittest
import math

from tuples import Point, Vector
from color import Color
from material import Material
from light import PointLight, lighting

class TestMaterial(unittest.TestCase):

    def assertColorEqual(self, c1, c2):
        self.assertAlmostEqual(c1.r, c2.r)
        self.assertAlmostEqual(c1.g, c2.g)
        self.assertAlmostEqual(c1.b, c2.b)

    def test_default_material(self):
        m = Material()
        self.assertEqual(m.color, Color(1, 1, 1))
        self.assertEqual(m.ambient, 0.1)
        self.assertEqual(m.diffuse, 0.9)
        self.assertEqual(m.specular, 0.9)
        self.assertEqual(m.shininess, 200)

    def test_light_and_eye_perpendicular(self):
        m = Material()
        position = Point(0 , 0, 0)
        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = PointLight(Point(0, 0, -10), Color(1, 1, 1))
        result = lighting(m, light, position, eyev, normalv)
        self.assertEqual(result, Color(1.9, 1.9, 1.9))

    def test_light_perpendicular_and_eye_at_45(self):
        r = math.sqrt(2) / 2
        m = Material()
        position = Point(0 , 0, 0)
        eyev = Vector(0, r, -r)
        normalv = Vector(0, 0, -1)
        light = PointLight(Point(0, 0, -10), Color(1, 1, 1))
        result = lighting(m, light, position, eyev, normalv)
        self.assertEqual(result, Color(1.0, 1.0, 1.0))

    def test_light_at_45_and_eye_perpendicular(self):
        r = math.sqrt(2) / 2
        m = Material()
        position = Point(0 , 0, 0)
        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = PointLight(Point(0, 10, -10), Color(1, 1, 1))
        result = lighting(m, light, position, eyev, normalv)
        x = 0.7363961
        self.assertColorEqual(result, Color(x, x, x))

    def test_light_at_45_and_eye_at_neg_45(self):
        r = math.sqrt(2) / 2
        m = Material()
        position = Point(0 , 0, 0)
        eyev = Vector(0, -r, -r)
        normalv = Vector(0, 0, -1)
        light = PointLight(Point(0, 10, -10), Color(1, 1, 1))
        result = lighting(m, light, position, eyev, normalv)
        x = 1.6363961
        self.assertColorEqual(result, Color(x, x, x))

    def test_light_directly_behind_surface_and_eye(self):
        m = Material()
        position = Point(0 , 0, 0)
        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = PointLight(Point(0, 0, 10), Color(1, 1, 1))
        result = lighting(m, light, position, eyev, normalv)
        self.assertEqual(result, Color(0.1, 0.1, 0.1))

