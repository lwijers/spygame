''' ---spygmae2d_versieIII---, created by Lennart on 3/6/2018'''


import _state_template

#---------------------------------------------------------------------------------------
# SHARED STATES
#---------------------------------------------------------------------------------------

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
        pass#self.actor.pathfinder.find_path()

    def check_conditions(self):
        if self.actor.target == None:
            return 'idle'


    def do_actions(self):
        self.actor.motor.move()

    def exit_actions(self):
        pass

#----------------------------------------------------------------------------------------------

class Distraction(_state_template.State):
    def __init__(self, actor):
        _state_template.State.__init__(self, 'distraction')
        self.actor = actor
        self.subject = None
        self.talking_distance = 50

    def entry_actions(self):

        self.subject = self.actor.subject
        self.subject.brain.set_state('waiting_for_interaction')


    def check_conditions(self):
        if abs(self.actor.rect.centerx -
                       self.subject.rect.centerx) > self.talking_distance:
            return 'move_to'

    def do_actions(self):

        if self.actor.rect.centerx > self.subject.rect.centerx:
            self.actor.set_path_to((self.subject.rect.centerx + self.talking_distance,
                                    self.subject.rect.centery))
        if self.actor.rect.centerx < self.subject.rect.centerx:
            self.actor.set_path_to((self.subject.rect.centerx - self.talking_distance,
                                    self.subject.rect.centery))
        if self.actor.target:
            self.actor.motor.move()
