import pygame

from main._const import *
from movement import _motor
from movement import _pathfinder
from state_machine import _state_machine
from ui import _action_menu

class Creature_template():
    def __init__(self, world, pos, type):
        self.world = world
        self.grid = world.grid
        self.type = type
        self.pos = pos
        self.y = 0
        self.w = SM_CELL_SIZE
        self.h = SM_CELL_SIZE * 3
        self.rect = pygame.Rect((0,0), (self.w, self.h))
        self.rect.midbottom = self.pos
        self.color = PURPLE
        self.current_tile = []
        self.set_cur_tile()
        self.goal = ()
        self.move_speed = 1.5

        # self.is_selectable_by_box = True

        self.mouse_hover = False

        self.pathfinder = _pathfinder.Pathfinder(self.world, self)
        self.target = None
        self.motor = _motor.Motor(self)
        self.brain = _state_machine.create_state_machine(self)
        self.selected = False

        self.subject = None

        self.possible_interactions = []

    def set_target(self):
        self.target = self.pathfinder.pop_node()

    def set_cur_tile(self):
        # records in which tile the character is
        self.current_tile = self.world.grid.get_walk_tile(self.rect.midbottom)

    def set_selected(self, selected):
        # turns selected on and off
        if selected :
            self.selected = True
        else:
            self.selected = False

    def set_subject(self, subject):
        self.subject = subject

    def remove_subject(self):
        self.subject = None

    def give_possible_actions(self):
        return self.possible_interactions

    def on_click(self, mouse_pos):
        pass

    def on_r_click(self):
        pass

    def on_r_click_on_self(self, clicker):
        pass

    def on_mouse_hover(self, mouse_pos):
        pass

    def set_path_to_mouse(self):
        pos = pygame.mouse.get_pos()
        self.pathfinder.set(
            (self.current_tile,
            (pos[0], self.grid.get_floor_y(pos))))

        self.set_target()

    def set_path_to(self, pos):
        self.pathfinder.set(
            (self.current_tile,
             (pos[0], self.grid.get_floor_y(pos))))

        self.set_target()

    def update(self):
        self.brain.think()
        self.set_cur_tile()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

        if self.selected:
            pygame.draw.rect(screen, YELLOW, self.rect, 2)


# -----------------------------------------------------------------------------------
# player character
# -----------------------------------------------------------------------------------


class Player_character(Creature_template):
    def __init__(self, world, pos):
        Creature_template.__init__(self, world, pos, "pl_character")
        self.stats = {'smarts': 6,
                      'strength': 4}

        # used if right clicked on self
        self.possible_interactions = {"jerk _off" : {'req' : None}}

        # ties interactions to functions
        self.all_interactions = {
            "jerk _off": {self.jerk_off : None},
            "move_here": {self.move_to : None},
            "distract": {self.distract : None}
        }

    def check_poss_interactions(self, interactions, stats_interactee):
        possible = {}
        for interaction, values in interactions.iteritems():
            if values['req'] :

                for stat, check  in values['req'].iteritems():
                    if self.stats[stat] >= self.subject.stats[check]:
                        possible[interaction] = self.all_interactions[interaction]
            else:
                possible[interaction] = self.all_interactions[interaction]
        self.possible_actions = possible


    def on_r_click(self):

        if not self.subject:
            self.set_path_to_mouse()

        else:
            if hasattr(self.subject, "possible_interactions"):

                self.check_poss_interactions(self.subject.possible_interactions,
                                             self.subject.stats)

                self.world.add_menu(_action_menu.Action_menu(
                    pygame.mouse.get_pos(), self.possible_actions, self.world))

            # self.set_subject(None)
            # self.set_selected(False)


    def update(self):
        self.brain.think()
        self.set_cur_tile()


        # self.world.debug.push_items(self)


    def move_to(self):
        print 'moving to'
        self.pathfinder.set(
            (self.current_tile,
             (self.subject.rect.centerx,
              self.grid.get_floor_y(self.subject.rect.center))))

        self.set_target()
        self.remove_subject()
        self.world.sel_mgr.set_actor(self)
        self.set_selected(True)

    def jerk_off(self):
        print('jerking off, character 165')
        self.remove_subject()
        self.world.sel_mgr.reset_actor()

    def distract(self):
        print 'distracting, characters 159'
        self.brain.set_state('distraction')
        self.remove_subject()
        self.world.sel_mgr.reset_actor()

    def talk(self):
        print 'talking, characters 163'
        self.remove_subject()
        self.world.sel_mgr.reset_actor()
# -----------------------------------------------------------------------------------
# ENEMY
# -----------------------------------------------------------------------------------


class Enemy(Creature_template):
    def __init__(self, world, pos,  subclass):
        Creature_template.__init__(self, world, pos, "enemy")
        self.color = RED
        self.subclass = subclass
        self.stats = {'smarts' : 5,
                      'strength' : 5}

        self.possible_interactions = {
            'distract': {'req': {'smarts': 'smarts'}},
            'move_here': {"req": None}
            }



    def update(self):
        self.brain.think()
        self.set_cur_tile()

