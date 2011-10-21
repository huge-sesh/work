import math

class vector(tuple):
    def __new__(cls, *args):
        #pack args into list, which tuple() likes
        assert len(args) == 2, "this is a 2d game, not "+ len(args)+"d"
        return super(vector, cls).__new__(cls, args)

    def __add__(self, other):
        return vector(self[0] + other[0], self[1] + other[1])
    def __radd__(self, other):
        return vector(self[0] + other[0], self[1] + other[1])

    def __sub__(self, other):
        return vector(self[0] - other[0], self[1] - other[1])
    def __rsub__(self, other):
        return vector(other[0] - self[0], other[1] - self[1])

    def __mul__(self, other):
        assert type(other) in (int, float), 'cant multiply vector by %s' %type(other)
        return vector(self[0] * other, self[1] * other)
    def __rmul__(self, other):
        assert type(other) in (int, float), 'cant multiply vector by %s' %type(other)
        return vector(self[0] * other, self[1] * other)

    def __div__(self, other):
        assert type(other) in (int, float), 'cant divide vector by %s' %type(other)
        return vector(self[0] / other, self[1] / other)
    def __rdiv__(self, other):
        assert type(other) in (int, float), 'cant divide vector by %s' %type(other)
        return vector(other / self[0], other / self[1])

    def __floordiv__(self, other):
        assert type(other) in (int, float), 'cant divide vector by %s' %type(other)
        return vector(self[0] // other, self[1] // other)
    def __rfloordiv__(self, other):
        assert type(other) in (int, float), 'cant divide vector by %s'%type(other)
        return vector(other // self[0], other // self[1])

    def __neg__(self):
        return vector(-self[0], -self[1])

    def __abs__(self):
        return math.sqrt(self[0]**2 + self[1]**2)

    def sq_norm(self):
        return self[0]**2 + self[1]**2

    def normal(self):
        return vector(-self[1], self[0])

    def unit_normal(self):
        return self.normal() / abs(self)

    def dot(self, other):
        return self[0] * other[0] + self[1] * other[1]

    def unit(self):
        return self / abs(self)

    def is_zero(self):
        return self[0] == 0 and self[1] == 0

    def round(self):
        return vector(int(self[0] + 0.5), int(self[1] + 0.5))
