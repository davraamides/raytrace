from color import Color

class Material(object):
    def __init__(self):
        self.color = Color(1, 1, 1)
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200

    def __eq__(self, other):
        return self.color == other.color \
            and self.ambient == other.ambient \
            and self.diffuse == other.diffuse \
            and self.specular == other.specular \
            and self.shininess == other.shininess


