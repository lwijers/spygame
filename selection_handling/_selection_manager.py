''' ---spygmae2d_versieIII---, created by Lennart on 3/6/2018'''
import pygame
from _const import *
import _selection_box


class Selection_manager():
    def __init__(self, world):
        self.world = world
        self.interactables = []

        self.all_items = self.world.give_all_items()
        self.current_selected = []
        self.actor = None
        # self.subject = None
        self.mouse_over_list = []
        self.mouse_over_object = None
        self.sel_box = _selection_box.Selection_box()


    def add_item(self, item):
        self.all_items.append(item)

    def remove_item(self, item):
        self.all_items.remove(item)

    def set_selected(self):
        """controls the order of importance of selection box
        and sets items to selected"""

        # empty list
        self.current_selected = []


        for item in self.interactables:
            # check if interactible is hit by selection box
            if self.sel_box.give_selection_area().colliderect(item.rect):
                # if hit append to list
                self.current_selected.append(item)
            # if not hit make sure the item sets to not selected
            else:
                item.set_selected(False)

        # make lists to order importance of selection
        player = []
        enemy = []
        other = []

        # if multiple type of items are selected, order of importance is:
        # player, enemies, objects

        # filter the items from entire selection
        for item in self.current_selected:
            if item.__class__.__name__ == "Player_character":
                player.append(item)
            if item.__class__.__name__ == "Enemy":
                enemy.append(item)
            if item.__class__.__name__ == "Action_menu":
                pass
            else:
                other.append(item)

            # loop and find the first list of importance
            for item in [player, enemy, other]:
                if item:
                    self.current_selected = item
                    break

        # set all selected items to "selected"
        for item in self.current_selected:
            item.set_selected(True)

        if self.current_selected:
            if len(self.current_selected) > 1:
                print "72 sel mgr not yet implemented"
            else:
                self.actor = self.current_selected[0]

    def reset_actor(self):
        self.actor = None

    def set_actor(self, actor):
        self.actor = actor
    # MOUSE ACTIONS----------------------------------------------------------------------------------

    def check_mouse_over(self, events, mouse_pos):
        """"checks in clickables and selectables if there is a hover, appends
        them to the current_hovering list. Returns first item,
        gives empty list otherwise. Activates the on_mouse_hover of the item"""

        for item in self.all_items:
            if getattr(item, 'rect', False):
                if item.rect.collidepoint(mouse_pos):
                    if getattr(item, 'on_mouse_hover', False):
                        item.on_mouse_hover(mouse_pos)
                    self.mouse_over_list.append(item)

        if self.mouse_over_list:
            self.mouse_over_object = self.mouse_over_list[0]
        else:
            self.mouse_over_object = None

    def l_down(self):
        # check if the selection box can be added to the world
        if self.sel_box not in self.world.selection_box:
            self.world.add_sel_box(self.sel_box)

    def l_clicked(self):

        self.actor = []

        if self.sel_box.activated:
            self.sel_box.selection_made()
            self.world.remove_sel_box(self.sel_box)
            self.set_selected()

        if self.actor:
            # make sure the quick menu processes the click if there is one
            for menu in self.world.menus:
                menu.on_click(pygame.mouse.get_pos())

    def r_clicked(self):
        if len(self.current_selected) > 1:
            print "122 sel mgr,  multiple selection actions not yet implemented"

        if self.world.menus:
            if not self.world.menus[0].rect.collidepoint(pygame.mouse.get_pos()):
                self.actor.set_subject(None)
                self.reset_actor()
                self.world.menus[0].clean_up()

        # if there is an actor selected
        if self.actor:

            # and there is a right click on a possible subject
            for interactable in self.interactables:
                if interactable.rect.collidepoint(pygame.mouse.get_pos()):
                    self.actor.set_subject(interactable)

            self.actor.on_r_click()




            # do actions (actor calculates which one)




            # PUD ----------------------------------------------------------------------------------
            # set subject to actor

    def process_input(self, events):
        mouse_pos = pygame.mouse.get_pos()

        # check if a selection box is made

        # Resets the mouse_over_list
        self.mouse_over_list = []
        # check if there is a mouse over on an item
        self.check_mouse_over(events, mouse_pos)

        # if there is a click inside the playin area
        if self.world.grid.total_rect.collidepoint(pygame.mouse.get_pos()):

            if events.mouse.l_down:
                self.l_down()

            if events.mouse.l_clicked:
                self.l_clicked()

            if events.mouse.r_clicked:
                self.r_clicked()

    def update(self):

        self.all_items = self.world.give_all_items()
        self.interactables = self.world.give_interactables()

        #
        # self.world.debug.push_items( {#"interactables" : self.interactables,
        #     # "current selected" : self.current_selected,
        #     "actor" : self.actor})
        #
        # # "mouse_over_list": self.mouse_over_list,
        # # "hovering over": self.mouse_over_object})
        #
