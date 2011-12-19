import pygame
import world, game

class Edge(object):
    def __init__(self, origin, end):
        self.origin = origin
        self.end = end
        self.recalculate()
        self.active = False
        manager.add(self)

    def recalculate(self):

        self.n = (self.end - self.origin).unit_normal()
        self.D = -((self.origin).dot(self.n))

        self.vector = (self.end - self.origin).unit()
        self.max = abs(self.end - self.origin)


    def collide_point(self, point, velocity):
        if not self.active: return None
        assert velocity > 0, 'why would you check collision on a non-moving object'
        if self.n.dot(velocity) >= 0: 
            return None
        d0 = self.n.dot(point) + self.D
        d1 = self.n.dot(point + velocity) + self.D
        if d0 * d1 > 0:
            return None

        if (d0 == 0 or d1 == 0) and velocity.dot(self.n) > 0: 
            return None

        if d0 == d1: 
            return None

        u = (d0 / (d0 - d1))
        projection = self.vector.dot((point + velocity * u) - self.origin)

        if projection >= 0 and projection <= self.max: return u
        else:
            return None

    def __repr__(self):
        return 'Edge[%s,%s]' % (self.origin, self.end)

    def key(self):
        return ((self.origin[0], self.origin[1]), (self.end[0], self.end[1]))
    def rkey(self):
        return ((self.end[0], self.end[1]), (self.origin[0], self.origin[1]))

class Manager:
    def __init__(self):
        self.edges = {}
    def add(self, edge):
        assert edge.key not in self.edges, 'adding duplicate key'
        self.edges[edge.key()] = edge
        mirror = self.edges.get(edge.rkey(), None)
        if mirror:
            edge.active = False
            mirror.active = False
        else: edge.active = True

    def remove(self, edge):
        assert edge.key in self.edges, 'removed edge not in tree'
        assert edge == self.edges[edge.key()], 'removed edge but wrong edge was already in tree'

        del(self.edges[edge.key()])
        mirror = self.edges.get(edge.rkey(), None)
        if mirror: mirror.active = True


    def clear(self):
        self.edges = {}

    def render(self):
        for edge in self.edges.itervalues():
            if edge.active: color = pygame.Color(0, 255, 0, 0)
            else: color = pygame.Color(0, 0, 255, 0)
            pygame.draw.line(game.screen, color, edge.origin, edge.end, 4)

manager = Manager()
