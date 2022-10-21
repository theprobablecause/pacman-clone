import os
import pygame as pg
import play
from menu import Menu

class Game:
    RESOLUTION = (1280, 800)
    FRAMES_PER_SECOND = 60 # limit the game speed 
    FRAME_TIME = 1.0/FRAMES_PER_SECOND 
    PROJECT_DIR = os.path.join(os.path.dirname(__file__), os.pardir)

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(size=Game.RESOLUTION)
        self.frame_clock = pg.time.Clock()

    def run(self):
        while True: 
            g = Menu()
            g.main_menu()
            
    # Draw current display buffer to screen, then wait for next frame.
    # NOTE: Call at the end of a frame process (end of the running loop)
    def wait_next_frame(self):
        pg.display.flip() # update the screen 
        self.frame_clock.tick(Game.FRAMES_PER_SECOND) # wait until next frame time