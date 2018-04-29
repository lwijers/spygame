import pygame

from main._const import *


class Room():
    def __init__(self, room_id):
        self.id = room_id
        self.rect = pygame.Rect(self.id[0] * L_CELL_SIZE_X,
                                self.id[1] * L_CELL_SIZE_Y,
                                L_CELL_SIZE_X,
                                L_CELL_SIZE_Y)
        self.is_accessible = True,
        self.tiles_contained = []

