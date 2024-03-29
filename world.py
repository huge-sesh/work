import pygame, time, pprint
import player, work, game, prefab, edge, block
from vector import vector

edges = edge.Manager()
background = pygame.Surface(game.screen.get_size()).convert()
background.fill((250, 250, 250))
player = prefab.make('player')
enemy = prefab.make('enemy')
enemy.pos = vector(200, 200)
player.pos = vector(316, 240)
gravity = vector(0, 500)

blocks = [block.Block(work.O(vector(x, y*32))) for y in range(480/32) for x in (0, 640-32)]
blocks += [block.Block(work.O(vector(x*32, y))) for y in (0, 480-32) for x in range(640/32)]
#blocks = [block.Block(work.O(vector(316, 332)))]
#blocks = [block.Block(work.O(vector(348, 332)))]

def update():
    game.screen.blit(background, (0, 0))
def pre_update(): pass
def post_update(): pass

def search(component, point, radius):
    ret = []
    for o in game.objects:
        if component in o.components:
            if abs(o.pos - point) <= radius:
                ret.append(o[component])
    return ret
