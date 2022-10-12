import os
import pygame as pg

import game_events as ge
from maze import Maze

RESOLUTION = (1280, 800)

class Game:
    FRAMES_PER_SECOND = 60
    PROJECT_DIR = os.path.join(os.path.dirname(__file__), os.pardir)

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(size=RESOLUTION)
        self.frame_clock = pg.time.Clock() # object that let's us maintain a framerate
        ## Running modes:
        # 0 = menu mode
        # 1 = play mode
        self.mode = 1 # CHANGE TO 0 WHEN MAIN MENU IS IMPLEMENTED

        # Play mode objects
        self.maze = Maze(game=self)

    def play(self):
        while True:
            ge.process_events(self)
            self.screen.fill((0, 0, 0))

            if self.mode == 0:
                pass # TODO: run menu code
            elif self.mode == 1:
                self.maze.update()
            
            pg.display.flip()
            self.frame_clock.tick(Game.FRAMES_PER_SECOND) # slow down game to framerate