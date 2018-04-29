import pygame

from main._const import *


class Ladder():
    def __init__(self, grid, start_rect):
        self.possible_interactions = {
            'move_here' : { "req" : None}
        }
        self.stats = {}
        self.grid = grid
        self.height = SM_CELL_SIZE * 6
        self.width = SM_CELL_SIZE
        self.rect = pygame.Rect(0,0, self.width, self.height)

        self.top_tile = start_rect
        self.rect.topleft = self.top_tile.topleft
        self.connected_tiles = []

        for tile in self.grid.tiles:
            if tile.rect.colliderect(self.rect):
                self.connected_tiles.append(tile)
                tile.is_accessible = True
        self.connected_tiles = sorted(self.connected_tiles)

        self.is_selectable_by_box = False

        # for tile in self.connected_tiles:
        #     print tile.id

        while len(self.connected_tiles) > 1:
            self.grid.add_connection(self.connected_tiles[0], self.connected_tiles[1])
            del self.connected_tiles[0]

    def process_input(self, events):
        pass
    def update(self):
        pass
    def on_mouse_hover(self, mouse_pos):
        pass
    def on_click(self, mouse_pos):
        pass
    def on_r_click(self):
        pass
    def switch_selected(self):
        pass
    def set_selected(self, selected):
        pass

    def draw(self, screen):
        # pass
        pygame.draw.rect(screen, BROWN, self.rect)
