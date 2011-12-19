import clock, work, world, pygame, edge
from vector import vector

size = (30, 30)

class Physics(work.Component):
    def __init__(self, obj, **kwargs):
        super(Physics, self).__init__(obj, **kwargs)
        self.velocity = vector(0,0)
        self.rect = pygame.Rect(0,0,30,30)
        #self.corners = (vector(0,0), vector(0,30), vector(30,30), vector(30,0))
        self.corners = (vector(16,16),)
        self.attached = None

    def accelerate(self, impulse):
        self.velocity = self.velocity + (impulse * clock.delta)

    def update(self):
        self.accelerate(world.gravity)
        #print 'pos %s velocity %s' %(self.pos, self.velocity)
        self.attached = None
        self.travel(1.0)

    def travel(self, timestep):
        if timestep <= 0 or self.velocity.is_zero(): 
            print "UNTRAVEL"
            return

        traveled = timestep
        hit = None
        for corner in self.corners:
            for ed in edge.manager.edges.itervalues():
                collision = ed.collide_point(self.pos + corner, self.velocity * timestep)
                if collision is not None: 
                    if hit == None or collision <= traveled:
                        hit = ed
                        traveled = timestep * collision
        
        future = self.pos + (self.velocity * traveled) + self.corners[0]
        if any((future.x < 32, future.x > 640-32)): print "PASS THROUGH X"
        if any((future.y < 32, future.y > 480-32)): print "PASS THROUGH Y"
        print self.pos + self.corners[0], self.velocity * traveled, traveled, future, hit

        self.pos = self.pos + (self.velocity * traveled)
        if hit:
            self.pos = self.pos.round() + hit.n
            direction = (hit.end - hit.origin).unit()
            self.velocity = direction * self.velocity.dot(direction)
            self.attached = hit
            print "RETRAVEL"
            self.travel(timestep - traveled)

