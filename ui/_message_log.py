''' ---spygmae2d_versieIII---, created by Lennart on 3/4/2018'''
import _text
import _timer
from main._const import *

all_messages = {
                'cant_walk_error' : "Can't walk there",
                "generic_error" : "Sorry, can't do that"
                }

class Message_log():
    def __init__(self, world, pos):
        self.pos = pos
        self.world = world
        self.messages = { }
        self.timer = _timer.Timer(self.world)
        self.message_id = 0

    def push_message(self, message):
        for label, text in all_messages.iteritems():
            if label == message:
                self.messages[label + str(self.message_id)] = text
                self.timer.set_alarm(label + str(self.message_id), 5000)
                self.message_id += 1

    def remove_message(self, message):
        del self.messages[message]

    def update(self):
        self.timer.update()
        alarm = self.timer.alarm()
        if alarm:
            self.remove_message(alarm)

    def draw(self, screen):
        if self.messages:
            t_pos = 0
            for message in self.messages:
                _text.write(screen, self.messages[message], (self.pos[0], self.pos[1] + t_pos), color = RED)
                t_pos += 15
