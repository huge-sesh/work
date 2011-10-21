import pygame, time
import player, work, game, prefab, edge, block
from vector import vector

edges = set()
background = pygame.Surface(game.screen.get_size()).convert()
background.fill((250, 250, 250))
player = prefab.make('player')
player.pos = vector(316, 240)
gravity = vector(0, 1000)

blocks = [block.Block(work.O(vector(x, y*32))) for y in range(480/32) for x in (0, 640-32)]
blocks += [block.Block(work.O(vector(x*32, y))) for y in (0, 480-32) for x in range(640/32)]
#blocks = [block.Block(work.O(vector(316, 264)))]

def update():
    game.screen.blit(background, (0, 0))
