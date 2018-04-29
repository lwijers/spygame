import pygame

import _items
from characters import _characters
from debug import _debug_menu
from grid import _grid
from main._const import *
from selection_handling import _selection_manager
from ui import _message_log

class World():
    def __init__(self):
        self.debug = _debug_menu.Debug_menu(self)


        self.grid = _grid.Grid()

        # will be constructed later from other lists, do not fill
        self.drawables = []
        self.updateables = []

        self.selection_box = []
        self.menus = []
        self.game_items = []



        self.speeds = [0, 1, 2, 3]
        self.cur_speed = 1
        self.sp_mod = self.speeds[self.cur_speed]

        self.message_log = _message_log.Message_log(self, (20, 0))


        self.characters = []
        self.add_pl_character(self.grid.get_tile_by_id((23,3)).walk_node)
        self.add_enemy(self.grid.get_tile_by_id((20,3)).walk_node, 'neighbour')

        self.ladder = _items.Ladder(self.grid, self.grid.get_tile_by_id((7,8)).rect)
        self.ladder2 = _items.Ladder(self.grid, self.grid.get_tile_by_id((12, 3)).rect)
        self.add_game_item(self.ladder)
        self.add_game_item(self.ladder2)

        self.sel_mgr = _selection_manager.Selection_manager(self)


# ADD--------------------------------------------------------------------------------

    def add_enemy(self, pos, en_type):
        enemy = _characters.Enemy(self, pos, en_type)
        self.characters.append(enemy)

    def add_game_item(self, g_item):
        self.game_items.append(g_item)

    def add_menu(self, menu):
        self.menus.append(menu)

    def add_pl_character(self, pos):
        self.characters.append(_characters.Player_character(self, pos))

    def add_sel_box(self, box):
        self.selection_box.append(box)


# REMOVE ------------------------------------------------------------------------

    def remove_game_item(self, g_item):
        self.game_items.remove(g_item)

    def remove_menu(self, menu):
        self.menus.remove(menu)

    def remove_sel_box(self, box):
        self.selection_box.remove(box)

# OTHER---------------------------------------------------------------------------------
    def give_all_items(self):
        return self.menus \
                + self.characters \
                + self.game_items \
                + self.grid.tiles \

    def give_interactables(self):
        return self.game_items \
               + self.characters \
               + self.menus


    def speed_selector(self):
        self.cur_speed += 1

        if self.cur_speed >= len(self.speeds):
            self.cur_speed = 0

        self.sp_mod = self.speeds[self.cur_speed]

# -----------------------------------------------------------------------------------
# PUD
# -----------------------------------------------------------------------------------

    def process_input(self, events):

        if events.keyboard.key_down(pygame.K_SPACE):
            self.speed_selector()

        if events.keyboard.key_down(pygame.K_d):
            self.debug.toggle_active()
            # self.debug.reset()

        self.debug.process_input(events)

        if self.sp_mod != 0:
            self.sel_mgr.process_input(events)


    def update(self):
        self.updateables =  self.game_items\
                            + self.characters \
                            + self.menus \
                            + self.selection_box \
                            + [self.message_log,
                               self.sel_mgr,
                               self.debug]


        self.drawables = [self.grid] \
                         + self.game_items \
                         + self.characters \
                         + self.menus \
                         + self.selection_box \
                         + [self.message_log,
                            self.debug]

        self.debug.set_debug_items(self.game_items + self.characters + self.menus +[self] )
        self.debug.update()

        if self.sp_mod != 0:
            for updateable in self.updateables:
                updateable.update()



    def draw(self, screen):




        screen.fill(BLACK)

        for drawable in self.drawables:
            drawable.draw(screen)

        # self .draw_sp_bubble( 100, 100, screen)
