''' ---spygmae2d_versieIII---, created by Lennart on 3/5/2018'''
import state_machine._pl_char_states
import state_machine._enemy_states

class State_machine(object):
    def __init__(self):

        self.states = {}
        self.active_state = None
        # self.ult_action = None

    def add_state(self, state):
        self.states[state.name] = state

    def think(self):
        if self.active_state is None:
            return
        self.active_state.do_actions()

        new_state_name = self.active_state.check_conditions()
        if new_state_name is not None:
            self.set_state(new_state_name)

    def set_state(self, new_state_name):
        if self.active_state is not None:
            self.active_state.exit_actions()

        self.active_state = self.states[new_state_name]
        self.active_state.entry_actions()

    def give_state(self):
        return self.active_state.name



    def draw_sp_bubble(self, x, y, screen):
        bubblex = x
        bubbley = y
        bw = 40
        bh = 25
        brect = pygame.Rect(bubblex, bubbley, bw, bh)

        pointlist = [brect.midbottom,
                     (brect.midbottom[0] -20 , brect.midbottom[1] + 10 ),
                     (brect.midbottom [0] -10, brect.midbottom[1])]

        pygame.draw.rect(screen, RED, (brect))
        pygame.draw.rect(screen, YELLOW, (bubblex, bubbley, bw, bh), 1)
        pygame.draw.polygon(screen, RED, pointlist)
        pygame.draw.polygon(screen, YELLOW, pointlist, 1)
        pygame.draw.rect(screen, RED, (brect.centerx - 10, brect.bottom -1,
                                       10, 2))

#--------------------------------------------------------------------------------
def create_state_machine(actor):
    st_mach = State_machine()

    states = {"pl_character" : [
                    state_machine._pl_char_states.Idle(actor),
                    state_machine._pl_char_states.Move_to(actor),
                    state_machine._pl_char_states.Distraction(actor)
                ],
                'enemy' : [
                    state_machine._enemy_states.Idle(actor),
                    state_machine._enemy_states.Move_to(actor),
                    state_machine._enemy_states.Wander(actor),
                    state_machine._enemy_states.Waiting_for_interaction(actor)
                    ]}



    for user, states  in states.iteritems():
        if actor.type == user:
            for state in states:
                st_mach.add_state(state)

    if actor.type == "enemy":
        st_mach.set_state('wander')
    else:
        st_mach.set_state('idle')

    return st_mach
#---------------------------------------------------------------------------------------
