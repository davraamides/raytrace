from tuples import Tuple, Point, Vector

class Ray(object):
    def __init__(self, origin, direction):
        if not Tuple.is_point(origin):
            raise ValeuError("Expected Point as first argument: {}".format(str(origin)))
        if not Tuple.is_vector(direction):
            raise ValeuError("Expected Vector as second argument: {}".format(str(direction)))
        self.origin = origin
        self.direction = direction

    def __repr__(self):
        return "ray(origin: {}, direction: {})".format(self.origin, self.direction)

    def position(self, t):
        return self.origin + self.direction * t