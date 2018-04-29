''' ---spygmae2d_versieIII---, created by Lennart on 3/7/2018'''
import pygame
from main._const import *
from ui import _buttons
# TODO if menu is open and right clicked somewhere else a new menu appears, not yet removed because it is dependent on the actor having a subject and subject needs to be passed to state machine

class Action_menu():
    def __init__(self, pos, actions, world):
        self.pos = pos
        self.possible_actions = actions
        self.world = world
        self.size = (0,0)
        self.padding = 10
        self.button_start_pos = (self.padding,self.padding)
        self.color = MENUCOLOR

        self.rect = pygame.Rect(self.pos, self.size)
        self.buttons = []
        self.mouse_hover = False


        for type, action  in self.possible_actions.iteritems():
            self.buttons.append(_buttons.Quick_button(
                (self.button_start_pos[0] + self.rect.x,
                self.button_start_pos[1] + self.rect.y),
                type, action))

            self.button_start_pos = (self.button_start_pos[0],
            self.button_start_pos[1] + (self.padding + self.buttons[0].size[1]))

        self.rect.size = ((self.padding *2) + self.buttons[0].size[0],
                          (self.padding * (len(self.buttons) +1)) + (len(self.buttons) *
                          self.buttons[0].size[1]))

        self.bg = pygame.Surface(self.rect.size)
        self.bg.fill(self.color)

        self.need_cleanup = False

    def set_selected(self, selected):
        pass

    def clean_up(self):
        self.world.remove_menu(self)
        # self.world.sel_mgr.reset_actor()

    def on_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            for button in self.buttons:
                if button.rect.collidepoint(mouse_pos):
                    button.on_click(mouse_pos)
                    # self.need_cleanup = True
        # else:
        self.clean_up()

    def on_r_click(self):
        pass
        # if not self.rect.collidepoint(mouse_pos):
        #     self.clean_up()

    def on_mouse_hover(self, mouse_pos):
        for button in self.buttons:
            button.on_mouse_hover(mouse_pos)

    def update(self):
        for button in self.buttons:
            button.update()
        if self.need_cleanup:
            self.clean_up()

    def draw(self, screen):
        screen.blit(self.bg, self.rect)
        for button in self.buttons:
            button.draw(screen)


