## This class will manage the main game play screen.
import pygame as pg
from pygame.surface import Surface

import game_events as ge
import maze as mz
import ghost as gh
from play_state import PlayState
import player
from sound import Sound
import scoreboard as sb

class Play:
    def __init__(self, app):
        self.app = app
        self.screen:Surface = app.screen
        self.scoreboard = sb.Scoreboard(play=self)
        self.maze = mz.Maze(play=self)
        self.play_state = PlayState(play=self)

        self.sound = Sound()

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

    def set_ghosts_mode(self, mode):
        for g in self.ghosts:
            g.set_mode(mode)

    def collision_check(self):
        cols = pg.sprite.spritecollide(self.player, self.ghosts, False)
        if len(cols) > 0:
            g = cols[0]
            self.player.ghost_interact(g)
    
    def reset(self):
        if self.player.lives >= 0:
            self.play_state.reset()
            self.player.reset()
            for g in self.ghosts:
                g.reset()

            self.play_state.action_pause(120)
        else:
            # GAME OVER
            self.play_state.action_pause(300)
            pass

    def run(self):
        self.play_state.action_pause(300)
        self.sound.music_normal()
        while True:
            self.screen.fill((0, 0, 0))
            ge.process_events(self)
            self.play_state.update()

            if not self.play_state.is_action_pausing:
                self.ghosts.update()
                self.player.update()
                self.collision_check()

            self.maze.draw()
            for g in self.ghosts:
                g.draw()
            self.player.draw()
            self.scoreboard.update()

            self.app.wait_next_frame()