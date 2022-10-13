## This class will manage the main game play screen.
from pygame.surface import Surface

import game_events as ge
import game
from maze import Maze

class Play:
    def __init__(self, game):
        self.game = game
        self.screen:Surface = game.screen
        self.maze = Maze(game=self.game)
    
    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            ge.process_events(self)
            self.maze.update()
            self.game.wait_next_frame()