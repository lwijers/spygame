''' ---spygmae2d_versieIII---, created by Lennart on 3/5/2018'''


class Motor():
    def __init__(self, actor):
        self.actor = actor
        self.rect = actor.rect
        self.node = ()
        self.move_speed = actor.move_speed * self.actor.world.sp_mod

        self.centerx = actor.rect.centerx
        self.bottom = actor.rect.bottom

    def set_node(self):
        self.node = self.actor.target

    def move(self):
        self.move_speed = self.actor.move_speed * self.actor.world.sp_mod
        self.set_node()



        if self.actor.target:
                # if you have to move horizontal
            if self.bottom == self.node[1]:

                # move right
                if self.centerx < self.node[0]:
                    if self.centerx + self.move_speed > self.node[0]:
                        self.centerx = self.node[0]
                    else:

                        self.centerx = self.centerx + self.move_speed

                # move left
                elif self.centerx > self.node[0]:
                    if self.centerx - self.move_speed < self.node[0]:
                        self.centerx = self.node[0]
                    else:

                        self.centerx = self.centerx - self.move_speed
                        # print self.centerx

            else:
                # move down
                if self.bottom < self.node[1]:
                    if self.bottom + self.move_speed > self.node[1]:
                        self.bottom = self.node[1]
                    else:
                        self.bottom += self.move_speed

                # move up
                else:
                    if self.bottom > self.node[1]:
                        if self.bottom - self.move_speed < self.node[1]:
                            self.bottom = self.node[1]
                        else:
                            self.bottom -= self.move_speed

            self.rect.centerx = self.centerx
            self.rect.bottom = self.bottom


            # remove node from list if node reached
            if self.rect.midbottom == self.node:
                self.actor.set_target()
