import math
from color import Color

class Light(object):
    pass

class PointLight(Light):
    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity


def lighting(material, light, point, eyev, normalv, components=False):
    black = Color(0, 0, 0)
    effective_color = material.color * light.intensity
    lightv = (light.position - point).norm()
    ambient = effective_color * material.ambient
    light_dot_normal = lightv.dot(normalv)
    if light_dot_normal < 0:
        diffuse = black
        specular = black
    else:
        diffuse = effective_color * material.diffuse * light_dot_normal
        reflectv = (-lightv).reflect(normalv)
        reflect_dot_eye = math.pow(reflectv.dot(eyev), material.shininess)
        if reflect_dot_eye <= 0:
            specular = black
        else:
            specular = light.intensity * material.specular * reflect_dot_eye

    if components:
        return ambient, diffuse, specular
    else:
        return ambient + diffuse + specular
