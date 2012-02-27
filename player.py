import pygame
from work import O, Component
from vector import vector
import resource, game, time, math, input, clock, movement, world


class Player(Component):
    def __init__(self, obj, **kwargs):
        super(Player, self).__init__(obj)
        self.movement = movement.Momentum()
        self.size = vector(32, 32)
        self.image = pygame.transform.scale(resource.get('characters')[0][0], self.size)
        self.keys = {}
        self.new_keys = set()
        print 'instantiated player'

    def bounce(self, direction):
        if self['Physics'].velocity.dot(direction) < 0:
            #reflect
            u = direction.normal()
            v = direction
            t = vector(self['Physics'].velocity.dot(u), -self['Physics'].velocity.dot(v))
            self['Physics'].velocity = vector(t.x * u.x + t.y * v.x, t.x * u.y + t.y * v.y) 
            self['Physics'].velocity += direction * self.movement.speed_bonus
        else:
            self['Physics'].velocity += direction * self.movement.speed_bonus

        
    def throw(self, direction):
        self['Physics'].velocity = direction * (abs(self['Physics'].velocity) + self.movement.speed_bonus)

    def pre_update(self):
        self.new_keys = set()

    def update(self):
        direction = vector(self.horizontal(), self.vertical())

        if input.JUMP in self.new_keys:
            enemies = world.search('Enemy', self.pos, self.size.x * 1.5)
            if enemies and not direction.is_zero():
                self.bounce(direction.unit())
                enemies[0].bounce(-direction.unit() * abs(self['Physics'].velocity))
        elif input.THROW in self.new_keys:
            enemies = world.search('Enemy', self.pos, self.size.x * 1.5)
            if enemies and not direction.is_zero():
                self.throw(direction.unit())
                enemies[0].throw(-direction.unit() * abs(self['Physics'].velocity))

        if self['Physics'].attached:
            direction = vector(self.horizontal(), self.vertical())
            if input.JUMP in self.keys:
                direction = direction + self['Physics'].attached.n
                if not direction.is_zero():
                    direction = direction.unit() * self.movement.jump_force
                    self['Physics'].velocity = self['Physics'].velocity + direction
            else:
                edge = self['Physics'].attached
                if not direction.is_zero(): 
                    direction = direction.unit()
                    direction = self['Physics'].attached.vector * direction.dot(self['Physics'].attached.vector)
                    direction = direction * abs(direction.dot(edge.vector)) * self.movement.acceleration(clock.delta)
                elif not self['Physics'].velocity.is_zero():
                    direction = - self['Physics'].velocity.unit() * self.movement.deceleration(clock.delta)
                    if direction.sq_norm() > self['Physics'].velocity.sq_norm(): 
                        direction = -self['Physics'].velocity

                self['Physics'].velocity = self['Physics'].velocity - self['Physics'].attached.n
                self.impulse(direction)
        else:
            self.impulse(vector(self.horizontal(), 0.0) * self.movement.air_acceleration(clock.delta))


    def impulse(self, velocity_delta):
        limit = max(abs(self['Physics'].velocity.x), self.movement.max_speed)
        if not velocity_delta.is_zero():
            new_velocity = self['Physics'].velocity + velocity_delta
            new_speed = abs(new_velocity)
            if new_speed > limit and self['Physics'].attached:
                new_velocity = new_velocity * (limit / new_speed)
            self['Physics'].velocity = new_velocity

    def render(self):
        game.screen.blit(self.image, self.pos)
        if self['Physics'].attached:
            pygame.draw.line(game.screen, pygame.Color(255, 0, 0, 0), self['Physics'].attached.origin, self['Physics'].attached.end, 8)

    def print_input(self):
        print vector(self.horizontal(), self.vertical())
        
    def key_down(self, key):
        if key in input.mapping:
            self.keys[input.mapping[key]] = clock.time
            self.new_keys.add(input.mapping[key])
        else:
            print key, 'not in mapping'

    def key_up(self, key):
        if key in input.mapping:
            if input.mapping[key] in self.keys:
                del(self.keys[input.mapping[key]])

    def most_recent(self, pos, neg):
        if pos in self.keys and neg in self.keys:
            return 1 if self.keys[pos] > self.keys[neg] else -1
        elif pos in self.keys: return 1
        elif neg in self.keys: return -1
        return 0

    def vertical(self): return self.most_recent(input.DOWN, input.UP)
    def horizontal(self): return self.most_recent(input.RIGHT, input.LEFT)
