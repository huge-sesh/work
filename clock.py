import pygame

clock = pygame.time.Clock()
clock.tick()
delta = 0.001
time = 0

def update():
    global delta, time
    delta = clock.tick() / 1000.0
    time += delta
