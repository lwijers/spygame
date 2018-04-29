import pygame
import random

import _room
from grid import _tile
from main._const import *


class Grid():
    def __init__(self):
        self.x_amount = SM_IN_L_CELL_X * X_AMOUNT_L
        self.y_amount = SM_IN_L_CELL_Y * Y_AMOUNT_L

        self.rooms = []
        self.build_room_grid()

        for room in self.rooms:
            if room.id == (3,1):
                room.is_accessible = False


        self.tiles = []
        self.build_tile_grid()

        self.assign_tiles_to_rooms()

        self.assign_floor_tiles()
        self.assign_walk_nodes()

        # self.connected_tiles = []
        self.initialize_connections()

        self.floor_y_positions = self.get_walk_y()

        self.total_rect = pygame.Rect(0,0, L_CELL_SIZE_X * X_AMOUNT_L, L_CELL_SIZE_Y * Y_AMOUNT_L)

    # ---------Initialization defs-------------

    def build_room_grid(self):
        for row in range(0, X_AMOUNT_L):
            for col in range(0, Y_AMOUNT_L):
                self.rooms.append(_room.Room((row, col)))


    def build_tile_grid(self):
        for row in range(0, self.x_amount):
            for col in range (0, self.y_amount):
                self.tiles.append(_tile.Tile((row, col)))

    def assign_tiles_to_rooms(self):
        # Check for every tile in which room it is and assign parent - child relation
        for tile in self.tiles:
            for room in self.rooms:
                # if the tile rect collides with the room rect
                if tile.rect.colliderect(room.rect):
                    # assign tile to room
                    room.tiles_contained.append(tile)
                    # assign room to tile
                    tile.parent_room = room
                    tile.is_accessible = room.is_accessible


    def assign_floor_tiles(self):
        # Check if bottom of room matches with bottom of tile and assign it as floor tile
        for room in self.rooms:
            for tile in self.tiles:
                if room.rect.bottom == tile.rect.bottom:
                    tile.is_floor = True
                    tile.is_accessible = False

    def assign_walk_nodes(self):
        for tile in self.tiles:
            walk_tile = ()
            if tile.is_floor:
                walk_tile = self.get_tile_by_id((tile.id[0], tile.id[1] -1))
                walk_tile.walk_node = walk_tile.rect.midbottom
                walk_tile.walkable = True


    def initialize_connections(self):
        # assigns the neighbours of the cells on the walking floors
        # right, left
        dirs = [1, -1]

        for tile in self.tiles:

            # check if the cell is a floor tile
            if tile.walkable:

                # identify the neighbour
                for dir in dirs:
                    connection = self.get_tile_by_id((tile.id[0] + dir, tile.id[1]))
                    # check if the neighbour existis in the grid
                    if connection:
                        # assign neighbour to current cell
                        tile.connections.append(connection)
                        # self.connected_tiles.append[tile] = contents


    # ---------------- Tool defs ----------------------
    def random_floor_point(self, cur_tile):
        # returns random point on current floor except points in current tile
        l = range(1, cur_tile.rect.left) + range(cur_tile.rect.right, (SW-1))
        return (random.choice(l), cur_tile.rect.bottom)

    def get_floor_y(self, pos):
        # returns the y pos of the inserted floor
        return self.get_room(pos).rect.bottom - (SM_CELL_SIZE)


    # def get_walk_tile(self, pos):
    #     # returns the y pos of the inserted floor
    #     return self.get_tile((pos[0], pos[1] - SM_CELL_SIZE ))

    def get_room(self, pos):
        for room in self.rooms:
            if room.rect.collidepoint(pos):
                return room

    def get_tile_by_id(self, tile_id):
        for tile in self.tiles:
            if tile.id == tile_id:
                return tile
        return False
        # print tile_id, tile.id


    def get_tile(self, pos):
        # gets tile from a x, y position
         for tile in self.tiles:
            if tile.rect.collidepoint(pos):
                return tile

    def get_walk_tile(self, pos):
        # gets tile from a x, y position
        for tile in self.tiles:
            if tile.rect.collidepoint((pos[0], pos[1]-1)):# and tile.walkable:
                return tile

    def get_neighbours(self, tile_id):
        # returns the neighbours of given tile
        for tile in self.tiles:
            if tile.id == tile_id:
                # print content['connections']
                return tile.connections

    def get_tile_center(self, tile_id):
        # returns center pos of given tile
        for tile in self.tiles:
            if tile.id == tile_id:
                return tile.rect.center

    def get_tile_midtop(self, tile_id):
        for tile in self.tiles:
            if tile.id == tile_id:
                return tile.rect.midtop

    def get_tile_midbottom(self, tile_id):
        for tile in self.tiles:
            if tile.id == tile_id:
                return tile.rect.midbottom

    def add_connection(self, tile1, tile2):
        tile1.connections.append(tile2)

        tile1.is_walkable = True
        tile1.walk_node = tile1.rect.midbottom

        tile2.connections.append(tile1)

    def get_walk_y(self):
        l = []
        for tile in self.tiles:
            if tile.id[0] == 0 and tile.walkable:
                l.append(tile.rect.midbottom[1])
        return l
    # ----------------- PUD -------------------------
    def draw(self, screen):
        for tile in self.tiles:
            if tile.is_accessible:
                pygame.draw.rect(screen, LIGHT_GREY, tile.rect)


            if tile.is_floor:
                pygame.draw.rect(screen, BROWN, tile.rect)
            # if tile.connections:
            #     pygame.draw.rect(screen, YELLOW, tile.rect)
            if not tile.is_accessible:
                pygame.draw.rect(screen, BLACK, tile.rect)
            pygame.draw.rect(screen, BLACK, tile.rect, 1)

        # for tile in self.tiles:
        #     if tile.walk_node:
        #         pygame.draw.circle(screen, RED, tile.walk_node, 2)

        for room in self.rooms:
            pygame.draw.rect(screen, DARK_GREY, room.rect, 1)

