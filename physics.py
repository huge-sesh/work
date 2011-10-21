import clock, work, world, pygame
from vector import vector

class Physics(work.Component):
    def __init__(self, obj, **kwargs):
        super(Physics, self).__init__(obj, **kwargs)
        self.velocity = vector(0,0)
        self.rect = pygame.Rect(0,0,31,31)
        self.corners = (vector(0,0), vector(0,31), vector(31,31), vector(31,0))
        self.attached = None

    def accelerate(self, impulse):
        self.velocity = self.velocity + (impulse * clock.delta)

    def update(self):
        self.accelerate(world.gravity)
        #print 'pos %s velocity %s' %(self.pos, self.velocity)
        self.attached = None
        self.travel(1.0)

    def travel(self, timestep):
        if timestep <= 0 or self.velocity.is_zero(): return

        traveled = 1.0
        hit = None
        for corner in self.corners:
            for edge in world.edges:
                collision = edge.collide_point(self.pos + corner, self.velocity * timestep)
                if collision is not None: 
                    if hit == None or collision <= traveled:
                        hit = edge
                        traveled = collision


        self.pos = self.pos + (self.velocity * traveled)
        if hit:
            self.pos = self.pos.round()
            direction = (hit.end - hit.origin).unit()
            self.velocity = direction * self.velocity.dot(direction)
            self.attached = hit
            self.travel(timestep - traveled)
