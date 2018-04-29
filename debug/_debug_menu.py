''' ---spygmae2d_versieIII---, created by Lennart on 3/10/2018'''
import pygame
from _const import *
from _debug_template import *
from debug._debug_main import Main_screen
from debug._debug_view import View_screen

class Debug_menu():
    def __init__(self, world):
        self.world = world
        self.rect = pygame.Rect(0,20, 400, 400)

        self.debug_items = []
        self.sorted_keys = []
        self.vars_to_track = []
        self.active = True

        self.screens = [View_screen(self, self.rect)]

        self.screen_stack = [self.screens[0]]

        self.inspected_item = None
        self.vars_to_view = {}

    def set_debug_items(self, items):
        self.debug_items = items

    def get(self, inst):
        return self.debug_items[inst]

    def reset_screen_stack(self):
        self.screen_stack = [self.screen_stack[0]]

    def set_var_to_view(self, name):
        self.vars_to_view[name] = {"par_class" : self.inspected_item}
                                 # "value": value}

    def remove_var_to_view(self, name):
        del self.vars_to_view[name]

    def add_var_to_view(self, par_class, name, value):
        self.vars_to_view[name] = {"par_class" : par_class,
                                 "value": value}

    def reset_vars_to_view(self):
        self.vars_to_view = {}

    def sort_list(self, dict):
        l = []
        for key in dict:
            l.append(key)
        return sorted(l)

    def push_screen(self, new_screen):
        for screen in self.screens:
            if screen.name == new_screen:
                self.screen_stack.append(screen)
                print self.screen_stack

    def push_new_screen(self, new_screen):
        self.screen_stack.append(new_screen)

    def set_active(self):
        if self.active:
            self.active = False
        else:
            self.active = True

    def process_input(self, events):
        if self.active:

            if events.mouse.l_clicked and self.rect.collidepoint(pygame.mouse.get_pos()):
                self.screen_stack[-1].on_l_click(pygame.mouse.get_pos())

    def update(self):
        if self.active:

            self.screen_stack[-1].update()

    def open_close_animation(self):
        pass

    def toggle_active(self):
        self.active = not self.active

    def draw(self, screen):
        if self.active:
            self.screen_stack[-1].draw(screen)


        pass

