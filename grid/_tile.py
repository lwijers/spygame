''' ---spygmae2d_versieIII---, created by Lennart on 3/4/2018'''
import pygame

from main._const import *


class Tile():
    def __init__(self, tile_id):
        self.id = tile_id
        self.rect = pygame.Rect(tile_id[0] * SM_CELL_SIZE,
                                tile_id[1] * SM_CELL_SIZE,
                                SM_CELL_SIZE,
                                SM_CELL_SIZE)
        self.connections = []
        self.parent_room = ()
        self.is_floor = False
        self.walkable = False
        self.walk_node = ()
        self.is_accessible = False


