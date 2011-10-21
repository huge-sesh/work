import work, pygame, game, edge, resource
from vector import vector

class Block(work.Component):
    def __init__(self, o):
        super(Block, self).__init__(o)
        corners = [vector(0,0), vector(0, 32), vector(32, 32), vector(32, 0)]
        corners = [o.pos + v for v in corners]
        self.edges = [edge.Edge(corners[i], corners[(i+1)%len(corners)]) for i in range(len(corners))]
        self.image = pygame.transform.scale(resource.get('blocks')[2][15], (32, 32))

    def render(self):
        game.screen.blit(self.image, self.pos)
