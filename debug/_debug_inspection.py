''' ---spygmae2d_versieIII---, created by Lennart on 3/10/2018'''
import pygame
from _const import *
from debug._debug_template import Debug_screen
from ui._text import write as write

class Inspection_screen(Debug_screen):
    def __init__(self, menu, rect):
        Debug_screen.__init__(self, menu, rect, 'inspection')

        self.title = "INSPECTION"


        self.leftcol =  pygame.Rect((self.contentrect.topleft,
                                     (self.line_spacing, self.contentrect.h)))

        self.middlecol = pygame.Rect(self.leftcol.topright,
                                     ((self.contentrect.w - self.line_spacing) /4,
                                    self.contentrect.h))

        self. rightcol = pygame.Rect(self.middlecol.topright,
                                     (self.contentrect.right - self.middlecol.right,
                                     self.contentrect.h))



        self.headers = {'VARIABLE NAME': self.middlecol,
                        'VALUE': self.rightcol}

        self.content_dict = {}


        self.buttons = {
            "BACK" : {
                "action" : None,
                "rect": pygame.Rect((self.but_start_x, self.but_start_y),
                                    self.but_size) },

            "MAIN" : {
                "action" : self.back_to_main,
                "rect": pygame.Rect((self.but_start_x + self.but_size[0] + self.line_spacing,
                                 self.but_start_y),
                                 self.but_size)}
             }



        ypos = self.header_space
        for var, val in vars(self.menu.inspected_item).iteritems():
            self.content_dict[var] = {'value': val,
                                  'rect': pygame.Rect(self.contentrect.x,
                                                      self.contentrect.y + ypos,
                                                      self.contentrect.width,
                                                      self.line_spacing),
                                  'selected': False}

            ypos += self.line_spacing

    def update(self):
        pass

    def back_to_main(self):
        # self.menu.reset_vars_to_view()
        # for name, var in self.content_dict.iteritems():
        #     if var["selected"] == True:
        #         self.menu.set_var_to_view(self.menu,
        #                                   name, var["value"])
        self.menu.reset_screen_stack()


    def c_on_l_click(self, pos):

        for name, val  in self.content_dict.iteritems():
            if name["rect"].collidepoint(pos):
                if name["selected"]:
                    self.menu.remove_var_to_view(var)
                    name["selected"] = False
                else:
                    name["selected"] = True
                    self.menu.add_var_to_view(name)



        for name, button in self.buttons.iteritems():
            if button["rect"].collidepoint(pos):
                button["action"]()





    def c_draw(self, screen):
        for header, rect in self.headers.iteritems():
            write(self.canvas, header, rect.topleft, font_cat = 'std_high')

        for var, contents in self.content_dict.iteritems():
            if contents['selected']:
                pygame.draw.rect(self.canvas, GREEN,
                                 (contents['rect'].topleft,
                                  (self.line_spacing, self.line_spacing)))
            else:
                pygame.draw.rect(self.canvas, RED,
                                 (contents['rect'].topleft,
                                  (self.line_spacing, self.line_spacing)))

            write(self.canvas, var, (self.middlecol.x, contents['rect'].y))
            write(self.canvas, contents['value'], (self.rightcol.x, contents['rect'].y))


