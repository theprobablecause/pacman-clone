## This class will manage the main game play screen.
from pygame.surface import Surface

import game_events as ge
import maze as mz
import ghost as gh

class Play:
    def __init__(self, game):
        self.game = game
        self.screen:Surface = game.screen
        self.maze = mz.Maze(game=self.game)

        self.player_speed = 4
        """The player's movement speed, in tiles per second."""

        self.ghosts_speed = 7
        """The ghosts' movement speed, in tiles per second."""

        self.test_ghost = gh.Blinky(maze=self.maze, play=self)
    
    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            ge.process_events(self)
            self.maze.update()
            self.test_ghost.update()
            self.game.wait_next_frame()