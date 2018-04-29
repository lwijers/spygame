
''' ---spygmae2d_versieIII---, created by Lennart on 3/4/2018'''


class Pathfinder():
    def __init__(self, world, actor):
        self.actor = actor
        self.message_log = world.message_log
        self.grid = world.grid
        self.start = ()
        self.goal = ()

        self.cur_path = []

    def set(self, (start, goal)):
        self.start = start
        self.goal = goal
        self.calc_path()

    def pop_node(self):
        if self.has_path():

            return self.cur_path.pop(0)
        else:
            return None

    def give_path(self):
        return self.cur_path

    def has_path(self):
        if self.cur_path:
            return True
        else:
            return False


    def calc_path(self):
        self.path = []
        self.endpoint = self.goal
        self.goal = self.grid.get_tile((self.goal[0], self.goal[1]-1))
        # self.endpoint = self.goal.rect.midbottom
        self.current = self.start
        self.frontier = [self.start]
        self.came_from = {}
        self.came_from[self.start] = None
        self.child = self.goal

        try:
            while self.frontier:
                if self.current == self.goal:
                    break


                for connection in self.current.connections:

                    if connection not in self.frontier and\
                                    connection not in self.came_from \
                                    and connection.is_accessible:
                        self.frontier.append(connection)
                        self.came_from[connection] = self.current

                self.frontier.pop(0)
                self.current = self.frontier[0]

            while self.child != self.start:
                parent = self.came_from[self.child]
                self.path.append(parent.walk_node)
                self.child = parent

            self.path.reverse()
            # # simplify the path to only the turnpoints (ex top of ladder)
            s_path = []

            if self.path:
                check = self.path[0]

                # remove al the horizontals except end tile
                for node in self.path:
                    if check[0] == node[0]:
                        s_path.append(check)
                        s_path.append(node)
                    check = node
                s_path.append(self.endpoint)

                # remove the first double
                s_path = s_path[2:]

                # remove the verticals except endpoints
                final_path = []
                for node in s_path:
                    if node[1] in self.grid.floor_y_positions:
                        final_path.append(node)
                self.cur_path = final_path

        except IndexError:
            # reset path so there are no nodes to use
            self.cur_path = False
            # push error message to log if not clicked on possible walkarea
            self.message_log.push_message('cant_walk_error')

