import pygame

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
JUMP = 5

mapping = {
    pygame.K_w : UP,
    pygame.K_s : DOWN,
    pygame.K_a : LEFT,
    pygame.K_d : RIGHT,
    pygame.K_SPACE : JUMP,
}
