import pygame
class Sheet(object):
    def __init__(self, name, tiles_x, tiles_y, tile_width, tile_height):
        self.surface = pygame.image.load(name).convert_alpha()
        self.tiles = []
        for x in range(tiles_x):
            self.tiles.append([])
            for y in range(tiles_y):
                tile = pygame.Surface((tile_width, tile_height))
                area = pygame.Rect(x*tile_width, y*tile_height, tile_width, tile_height)
                tile.blit(self.surface, (0,0), area=area)
                self.tiles[-1].append(tile)
        print 'loaded', name, len(self.tiles), len(self.tiles[0])
    def __getitem__(self, idx):
        return self.tiles[idx]
