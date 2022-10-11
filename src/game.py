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
        self.frame_clock = pg.time.Clock() # for maintaining a usable framerate
        self.maze = Maze(game=self)

    def play(self):
        while True:
            ge.process_events(self)
            self.screen.fill((0, 0, 0))

            # game logic
            self.maze.update()
            
            pg.display.flip()
            self.frame_clock.tick(Game.FRAMES_PER_SECOND)