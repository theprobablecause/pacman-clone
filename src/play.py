## This class will manage the main game play screen.
import pygame as pg
from pygame.surface import Surface

import game_events as ge
import maze as mz
import ghost as gh
import player

class Play:
    def __init__(self, game):
        self.game = game
        self.screen:Surface = game.screen
        self.maze = mz.Maze(game=self.game)

        self.player_speed = 7
        """The player's movement speed, in tiles per second."""

        self.ghosts_speed = 7
        """The ghosts' movement speed, in tiles per second."""

        self.player = player.Player(maze=self.maze, play=self)

        self.ghosts = pg.sprite.Group(
            gh.Blinky(maze=self.maze, pacman=self.player, play=self),
            gh.Inky(maze=self.maze, pacman=self.player, play=self),
            gh.Pinky(maze=self.maze, pacman=self.player, play=self),
            gh.Clyde(maze=self.maze, pacman=self.player, play=self)
        )

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            ge.process_events(self)
            self.maze.update()
            self.ghosts.update()
            self.player.update()
            self.game.wait_next_frame()