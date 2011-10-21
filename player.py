import pygame
from work import O, Component
from vector import vector
import resource, game, time, math, input, clock



max_speed = 20.0
acceleration = 10000.0
deceleration = 5000.0
jump_force = 10.0

class Player(Component):
    def __init__(self, obj, **kwargs):
        super(Player, self).__init__(obj)
        self.image = pygame.transform.scale(resource.get('characters')[0][0], (32, 32))
        self.keys = {}
        print 'instantiated player'

    def update(self):
        if self['Physics'].attached:
            velocity_delta = vector(self.horizontal(), self.vertical())
            if input.JUMP in self.keys:
                velocity_delta = velocity_delta + self['Physics'].attached.n
                if not velocity_delta.is_zero():
                    velocity_delta = velocity_delta.unit() * jump_force
                    self['Physics'].velocity = self['Physics'].velocity + velocity_delta
            else:
                edge = self['Physics'].attached
                if not velocity_delta.is_zero(): 
                    velocity_delta = velocity_delta.unit()
                    velocity_delta = self['Physics'].attached.vector * velocity_delta.dot(self['Physics'].attached.vector)
                    velocity_delta = velocity_delta * abs(velocity_delta.dot(edge.vector)) * acceleration * clock.delta
                elif not self['Physics'].velocity.is_zero():
                    velocity_delta = - self['Physics'].velocity.unit() * deceleration * clock.delta
                    if velocity_delta.sq_norm() > self['Physics'].velocity.sq_norm(): 
                        velocity_delta = -self['Physics'].velocity

                limit = max(abs(self['Physics'].velocity), max_speed)

                if not velocity_delta.is_zero():
                    new_velocity = self['Physics'].velocity + velocity_delta
                    new_speed = abs(new_velocity)
                    if new_speed > limit:
                        new_velocity = new_velocity * (limit / new_speed)
                    self['Physics'].velocity = new_velocity
                self['Physics'].velocity = self['Physics'].velocity - self['Physics'].attached.n

    def render(self):
        game.screen.blit(self.image, self.pos)

    def print_input(self):
        print vector(self.horizontal(), self.vertical())
        
    def key_down(self, key):
        if key in input.mapping:
            self.keys[input.mapping[key]] = clock.time
        else:
            print key, 'not in mapping'
        self.print_input()

    def key_up(self, key):
        if key in input.mapping:
            if input.mapping[key] in self.keys:
                del(self.keys[input.mapping[key]])
        self.print_input()

    def most_recent(self, pos, neg):
        if pos in self.keys and neg in self.keys:
            return 1 if self.keys[pos] > self.keys[neg] else -1
        elif pos in self.keys: return 1
        elif neg in self.keys: return -1
        return 0

    def vertical(self): return self.most_recent(input.DOWN, input.UP)
    def horizontal(self): return self.most_recent(input.RIGHT, input.LEFT)
