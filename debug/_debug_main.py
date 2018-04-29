import pygame

from debug._debug_template import Debug_screen
from ui._text import write as write
from debug._debug_inspection import Inspection_screen

class Main_screen(Debug_screen):
    def __init__(self, menu, rect):
        Debug_screen.__init__(self, menu, rect, 'main')

        self.title = "MAIN"

        self.debug_items = self.menu.debug_items



        self.leftrect =  pygame.Rect((self.contentrect.topleft,
                                      (self.contentrect.width / 4, self.contentrect.h)))
        self.rightrect = pygame.Rect(self.leftrect)
        self.rightrect.x = self.leftrect.right

        self.headers = {'NAME': self.leftrect,
                        'INSTANCE': self.rightrect}


        self.content_dict = {}
        self.coll_dict = {}


    def c_on_l_click(self, pos):
        for name, rect in self.coll_dict.iteritems():
            if rect.collidepoint(pos):
                self.menu.inspected_item = self.content_dict[name]
                self.menu.push_new_screen(Inspection_screen(self.menu, self.menu.rect))

    def update(self):
        it_id = 0
        ypos = self.header_space



        for item in self.menu.debug_items:

            self.content_dict[item.__class__.__name__ + "_"+str(it_id) ] = item



            self.coll_dict[item.__class__.__name__ + "_"+str(it_id)] = \
                pygame.Rect(self.contentrect.x,
                self.contentrect.y + ypos,
                self.contentrect.width,
                self.line_spacing)

            it_id += 1
            ypos += self.line_spacing



    def c_draw(self, screen):

        for header, rect in self.headers.iteritems():
            write(self.canvas, header, rect.topleft, font_cat = 'std_high')

        for name, item in self.content_dict.iteritems():
            write(self.canvas, name, (self.leftrect.x, self.coll_dict[name].top))
            write(self.canvas, item, (self.rightrect.x, self.coll_dict[name].top))
            # pygame.draw.rect(self.canvas, RED, self.coll_dict[name])






