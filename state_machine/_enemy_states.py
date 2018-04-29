''' ---spygmae2d_versieIII---, created by Lennart on 3/9/2018'''

import _timer
import _state_template

class Idle(_state_template.State):
    def __init__(self, actor):
        _state_template.State.__init__(self, 'idle')
        self.actor = actor

    def check_conditions(self):
        if self.actor.target != None:
            return 'move_to'

    def do_actions(self):
        pass

#-------------------------------------------------------------------------------------

class Move_to(_state_template.State):
    def __init__(self, actor):
        _state_template.State.__init__(self, 'move_to')
        self.actor = actor

    def entry_actions(self):
        pass

    def check_conditions(self):
        if self.actor.target == None:
            return 'idle'


    def do_actions(self):
        self.actor.motor.move()

    def exit_actions(self):
        pass

#---------------------------------------------------------------------------------------

class Wander(_state_template.State):
    def __init__(self, actor):
        _state_template.State.__init__(self, 'wander')
        self.actor = actor
        self.timer = _timer.Timer(self.actor.world)

    def entry_actions(self):
        self.actor.pathfinder.set((self.actor.current_tile,
                                  self.actor.grid.random_floor_point(
                                      self.actor.current_tile)))
        self.actor.set_target()

    def check_conditions(self):
        pass


    def do_actions(self):
        if self.actor.target == None and not self.timer.already_alarm('wait'):
            self.timer.set_alarm('wait',  2000)

        if self.timer.alarm():
            a = self.actor.grid.random_floor_point(
                                          self.actor.current_tile)

            self.actor.pathfinder.set((self.actor.current_tile,
                                      a))
            self.actor.set_target()

        self.timer.update()
        self.actor.motor.move()

class Waiting_for_interaction(_state_template.State):
    def __init__(self, actor):
        _state_template.State.__init__(self, 'waiting_for_interaction')
        self.actor = actor

    def entry_actions(self):
        self.actor.target = self.actor.set_path_to(self.actor.rect.center)

    def check_conditions(self):
        if self.actor.target != None:
            return 'move_to'



    def do_actions(self):
        pass