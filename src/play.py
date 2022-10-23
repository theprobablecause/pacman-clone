## This class will manage the main game play screen.
import pygame as pg
from pygame.surface import Surface

import game_events as ge
import maze as mz
import ghost as gh
import player
from sound import Sound

class Play:
    def __init__(self, app):
        self.app = app
        self.screen:Surface = app.screen
        self.maze = mz.Maze(play=self)

        self.sound = Sound()

        self.player_speed = 7.6
        """The player's movement speed, in tiles per second."""

        self.ghosts_speed = 7.6
        """The ghosts' movement speed, in tiles per second."""

        self.player = player.Player(maze=self.maze, play=self)

        self.ghosts = pg.sprite.Group(
            gh.Blinky(maze=self.maze, pacman=self.player, play=self),
            gh.Inky(maze=self.maze, pacman=self.player, play=self),
            gh.Pinky(maze=self.maze, pacman=self.player, play=self),
            gh.Clyde(maze=self.maze, pacman=self.player, play=self)
        )

    def run(self):
        self.sound.play_bg()
        while True:
            self.screen.fill((0, 0, 0))
            ge.process_events(self)
            self.maze.update()
            self.ghosts.update()
            self.player.update()
            self.app.wait_next_frame()