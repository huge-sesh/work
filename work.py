import pygame, time
import sheet, world, game
from vector import vector

class O(object):
    """gameobject"""
    def __init__(self, pos=vector(0,0)):
        self.rect = pygame.Rect(pos[0],pos[1],0,0)
        self.components = {}
        game.objects.add(self)

    def update(self):
        for component in self.components.itervalues(): component.update()

    def render(self):
        for component in self.components.itervalues(): component.render()

    def set_pos(self, val): self.rect = pygame.Rect(val[0],val[1], self.rect.width, self.rect.height)
    def get_pos(self): return vector(self.rect.x, self.rect.y)
    def set_size(self, val): self.rect = pygame.Rect(self.rect.x, self.rect.y, val[0], val[1])
    def get_size(self): return (self.rect.width, self.rect.height)

    pos = property(get_pos, set_pos)
    size = property(get_size, set_size)

    def __getitem__(self, idx): 
        try: return self.components[idx]
        except KeyError:
            print 'no %s in %s' % (idx, list(self.components.iterkeys()))
    def __setitem__(self, idx, val): self.components[idx] = val

class Component(object):
    """component"""
    def __init__(self, game_object, **kwargs):
        game_object[self.__class__.__name__] = self
        self.game_object = game_object
        for key, value in kwargs.iteritems(): setattr(self, key, value)

    def __getitem__(self, idx): return self.game_object[idx]
    def __setitem__(self, idx): self.game_object[idx] = val
    def get_pos(self): return self.game_object.pos
    def set_pos(self, pos): self.game_object.pos = pos
    def get_size(self): return self.game_object.size
    def set_size(self, size): self.game_object.size = size

    pos = property(get_pos, set_pos)
    size = property(get_size, set_size)

    def update(self): pass
    def render(self): pass

if __name__ == '__main__': game.run()
