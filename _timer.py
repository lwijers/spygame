''' ---spygmae2d_versieIII---, created by Lennart on 3/4/2018'''


import pygame


class Timer():
    def __init__(self, world):
        # self.clock = pygame.time.Clock()

        self.running = False

        self.timers = {}
        self.cur_alarm = None

        self.world = world

    def set_alarm(self, alarm_name, amount):
        '''takes amount in secs, converts to ms because self.secs is rounded down'''

        self.timers[alarm_name] = {'start_time' : pygame.time.get_ticks(),
                                   'time_elapsed' : 0,
                                   'goal_time' : amount}


    def process_input(self, events):
        pass

    def update(self):
        self.cur_alarm = None
        cur_time = pygame.time.get_ticks()
        for timer in self.timers:
            # take in account speed modifier
            self.timers[timer]['time_elapsed'] = ((cur_time - self.timers[timer]['start_time'])\
                                                  * self.world.sp_mod)


            if self.timers[timer]['time_elapsed'] > self.timers[timer]['goal_time']:
               self.cur_alarm = timer

    def alarm(self):

        if self.cur_alarm != None:
            del self.timers[self.cur_alarm]
            return self.cur_alarm
        else:
            return False

    def already_alarm(self, alarm):
        if alarm in self.timers:
            return True
        else:
            return False

    def draw(self, screen):
        pass