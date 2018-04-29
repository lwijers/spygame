import os

import pygame

import _world
from _const import *
from event_handling import _event_handler

os.environ['SDL_VIDEO_CENTERED'] = '0'

def run_game(width, height, fps):

    pygame.init()

    screen = pygame.display.set_mode( (width, height))#, pygame.FULLSCREEN)

    clock = pygame.time.Clock()
    #create the user interface, this creates the layout and widgets

    #create the event handler. This handles all input
    event_handler = _event_handler.Event_handler()

    running = True
    # images = _images.Images()

    World = _world.World()

    # main game loop
    while running:

        #let the event handler register inputs (for exiting, mouse input etc)
        event_handler.event_handling()
        World.process_input(event_handler)

        World.update()

        World.draw(screen)

        # update the screen
        pygame.display.flip()

        clock.tick( fps )


if __name__ == '__main__':
    run_game( SW, SH, FPS)