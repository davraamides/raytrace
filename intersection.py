
class Intersection(object):
    def __init__(self, t, obj):
        self.t = t
        self.object = obj

    def __repr__(self):
        return "intersection(object: {}, t: {})".format(self.object, self.t)


def hit(intersections):
    """Return closest intersection in positive t direction
    """
    if intersections:
        hits = sorted([_ for _ in intersections if _.t >= 0.0], key=lambda i: i.t)
        if hits:
            return hits[0]
    return None


