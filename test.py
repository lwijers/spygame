

class Debug_menu():
    def __init__(self, world):
        self.world = world
        self.start_pos = (5,30)
        self.active = False
        self.draw_dict = {}
        self.selected_class = None
        self.debugging_mode = 'top'

    def debugging_classes(self, class_list):
        i = 0
        id = 0
        to_debug = None

        if self.debugging_mode == 'top':
            to_debug = class_list

            for var in to_debug:

                self.draw_dict[var.__class__.__name__ + str(id)] =\
                    { 'var' : var,
                      'rect' :  pygame.Rect((self.start_pos[0], self.start_pos[1] + i),
                                (200, 15)),}
                i += 16
                id += 1


        else:
            to_debug = self.selected_class
            self.draw_dict = {}
            for name, item in vars(to_debug).iteritems():
                self.draw_dict[name] ={
                        'var' : item,
                        'rect': pygame.Rect((self.start_pos[0], self.start_pos[1] + i),
                            (200, 15))
                }

                i += 16
                id += 1

    def process_input(self, events):
        if self.active:
    #
    #         new_items = {}
            if events.mouse.l_clicked:
                for name, item in self.draw_dict.iteritems():
    #
                    if item['rect'].collidepoint(pygame.mouse.get_pos()):
                        self.selected_class  = item['var']
                        self.debugging_mode = 'other'

    def reset(self):
        self.debugging_mode = 'top'
        self.draw_dict = {}

    def toggle_active(self):
        self.active = not self.active

    def draw(self, screen):
        if self.active:
            for name, items in self.draw_dict.iteritems():
                pygame.draw.rect(screen, BLACK, items["rect"])
                _text.write(screen, (name, items),
                            (items["rect"].topleft),
                            color = (255,255, 0))
