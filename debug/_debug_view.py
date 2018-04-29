''' ---spygmae2d_versieIII---, created by Lennart on 3/10/2018'''
import pygame
from _const import *
from debug._debug_template import Debug_screen
from ui._text import write as write
from debug._debug_main import Main_screen

class View_screen(Debug_screen):
    def __init__(self, menu, rect):
        Debug_screen.__init__(self, menu, rect, 'view')

        self.title = "VIEW"


        self.leftrect =  pygame.Rect((self.contentrect.topleft,
                                      (self.contentrect.width / 4, self.contentrect.h)))
        self.rightrect = pygame.Rect(self.leftrect)
        self.rightrect.x = self.leftrect.right

        self.headers = {'NAME': self.leftrect,
                        'INSTANCE': self.rightrect}


        self.tab = 20

        self.content_dict = {}
        self.coll_dict = {}

        self.buttons = {

            "SELECT": {
                "action": self.goto_selection,
                "rect": pygame.Rect((self.buttonrect.left ,
                                     self.buttonrect.top),
                                    self.but_size)}
        }

    def goto_selection(self):
        print "aaa"
        self.menu.push_new_screen(Main_screen(self.menu, self.menu.rect))

    def c_on_l_click(self, pos):
        for name, button in self.buttons.iteritems():
            if button["rect"].collidepoint(pos):
                button["action"]()
        pass
        # for name, rect in self.coll_dict.iteritems():
        #     if rect.collidepoint((pos[0], pos[1] - self.y)):
        #         self.menu.inspected_item = self.content_dict[name]
        #         self.menu.push_new_screen(Inspection_screen(self.menu, self.menu.rect))

    def update(self):


        pass
        # it_id = 0
        # ypos = self.header_space
        #
        #
        #
        # for item in self.menu.debug_items:
        #
        #     self.content_dict[item.__class__.__name__ + "_"+str(it_id) ] = item
        #
        #
        #
        #     self.coll_dict[item.__class__.__name__ + "_"+str(it_id)] = \
        #         pygame.Rect(self.contentrect.x,
        #         self.contentrect.y + ypos,
        #         self.contentrect.width,
        #         self.line_spacing)
        #
        #     it_id += 1
        #     ypos += self.line_spacing
        #
        #

    def c_draw(self, screen):
        ypos = self.header_space

        for name, instance in self.menu.vars_to_view.iteritems():
            write(self.canvas, instance["par_class"], (self.contentrect.x,
                                                       self.contentrect.y + ypos))
            ypos += self.line_spacing

            write(self.canvas, name, (self.contentrect.x + self.tab,
                                                   self.contentrect.y + ypos))
            # for debug_item in self.menu.debug_items:
            #     if debug_item == instance["par_class"]:

            write(self.canvas, vars(instance["par_class"])[name],
                    (self.contentrect.x +100 + self.tab,
                    self.contentrect.y + ypos))

            ypos += self.line_spacing

        # for header, rect in self.headers.iteritems():
        #     write(self.canvas, header, rect.topleft, font_cat = 'std_high')
        #
        # for name, item in self.content_dict.iteritems():
        #     write(self.canvas, name, (self.leftrect.x, self.coll_dict[name].top))
        #     write(self.canvas, item, (self.rightrect.x, self.coll_dict[name].top))
        #     # pygame.draw.rect(self.canvas, RED, self.coll_dict[name])


