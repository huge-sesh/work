import world

class Edge(object):
    def __init__(self, origin, end):
        self.origin = origin
        self.end = end
        self.recalculate()
        world.edges.add(self)

    def recalculate(self):

        self.n = (self.end - self.origin).unit_normal()
        self.D = -((self.origin).dot(self.n))

        self.vector = (self.end - self.origin).unit()
        self.max = abs(self.end - self.origin)


    def collide_point(self, point, velocity):
        assert velocity > 0, 'why would you check collision on a non-moving object'
        d0 = self.n.dot(point) + self.D
        d1 = self.n.dot(point + velocity) + self.D
        if d0 * d1 > 0:
            return None

        if (d0 == 0 or d1 == 0) and velocity.dot(self.n) > 0: return None

        if d0 == d1: return None

        u = (d0 / (d0 - d1))
        projection = self.vector.dot((point + velocity * u) - self.origin)

        if projection > 0 and projection < self.max: return u
        else:
            return None

    def __repr__(self):
        return 'Edge[%s,%s]' % (self.origin, self.end)
