''' ---spygmae2d_versieIII---, created by Lennart on 3/8/2018'''
import pygame
from _const import *
from ui._text import write as write

import pygame

class Debug_screen():
    def __init__(self, menu, rect, name):
        self.menu = menu
        self.name = name
        self.x = rect.x
        self.y = rect.y
        self.w = rect.w
        self.h = rect.w


        self.title_f_size = 30
        self.text_f_size = 13

        self.high_color = (255, 255, 50)
        self.text_color = (255,255,255)
        padding = 10

        self.line_spacing = 14

        self.header_space = 15




        titleperc = 0.10
        contperc = 0.80
        buttperc= 0.10



        self.canvasrect = pygame.Rect((0, 0),
                    (self.w, self.h))

        self.mainrect = pygame.Rect((0 + padding, 0 + padding),
                                       (self.w - (2* padding), self.h - (2* padding)))

        self.titlerect = pygame.Rect(self.mainrect.topleft,
                                     (self.mainrect.width, int(self.mainrect.h * titleperc) ))

        self.contentrect = pygame.Rect((self.mainrect.left, self.titlerect.bottom),
                                       (self.mainrect.width, int(self.mainrect.h * contperc) ))

        self.buttonrect = pygame.Rect((self.mainrect.left, self.contentrect.bottom),
                                       (self.mainrect.width, int(self.mainrect.h * buttperc)))

        self.rects = [self.buttonrect, self.contentrect,  self.titlerect, self.canvasrect,  self.mainrect ]

        #

        self.canvas = pygame.Surface(self.canvasrect.size).convert()

        self.canvas.set_alpha(175)

        self.buttons = {}
        self.but_size = (100, 75)
        self.but_start_x = self.buttonrect.left
        self.but_start_y = self.buttonrect.top

    def update(self):
        pass

    def on_l_click(self, m_pos):
        pos = (m_pos[0], m_pos[1] - self.y)
        self.c_on_l_click(pos)

    def draw(self, screen):

        self.canvas.fill((0, 0, 0))
        write(self.canvas, self.title, (self.titlerect.centerx,self.titlerect.centery + 3) , font_cat = 'hdr', centered = True)

        # ypos =
        for name, button in self.buttons.iteritems():
            write(self.canvas, name, button["rect"].center, centered = True)


        self.c_draw(screen)
        screen.blit(self.canvas, (self.x, self.y))











