''' ---spygmae2d_versieIII---, created by Lennart on 3/4/2018'''
import pygame


class Selection_box():
    def __init__(self):
        self.mouse_start = ()
        self.activated = False
        self.sel_rect = pygame.Rect(0,0,0,0)
        self.latest_selection = []
        self.selected_area = None

    def update(self):
        if not self.activated:
            self.mouse_start = pygame.mouse.get_pos()

        if pygame.mouse.get_rel() != (0,0):
            self.activated = True
            self.sel_rect.topleft = (min(self.mouse_start[0], pygame.mouse.get_pos()[0]),
                                 min(self.mouse_start[1], pygame.mouse.get_pos()[1]))

            self.sel_rect.size = (abs(self.mouse_start[0] - pygame.mouse.get_pos()[0]),
                                  abs(self.mouse_start[1]- pygame.mouse.get_pos()[1]))

    def selection_made(self):
        self.selected_area = pygame.Rect(self.sel_rect)
        self.activated = False

    def give_selection_area(self):
        return self.selected_area

    def draw(self, screen):
        selector = pygame.Surface(self.sel_rect.size)
        selector.set_alpha(150)
        selector.fill((200,200,200))
        selector.convert()
        if self.activated == True:
            pygame.draw.rect(selector, (150,150,150), pygame.Rect((0, 0), self.sel_rect.size), 2)
            screen.blit(selector, self.sel_rect)
