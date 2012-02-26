import pygame, time
import game, world, edge
from vector import vector

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('work')
objects = set()

def run():
    done = False
    while not done:
        pre_update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                world.player['Player'].key_down(event.key)
            elif event.type == pygame.KEYUP:
                world.player['Player'].key_up(event.key)

        update()
        render()
        pygame.display.flip()
        post_update()
    print 'pg.quit'
    pygame.quit()

def update():
    world.update()
    for obj in objects: obj.update()

def pre_update():
    world.pre_update()
    for obj in objects: obj.pre_update()

def post_update():
    world.post_update()
    for obj in objects: obj.post_update()

def render():
    for obj in objects: obj.render()
    edge.manager.render()

if __name__ == '__main__': game.run()
