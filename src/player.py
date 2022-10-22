import random
import pygame as pg
from pygame.sprite import Sprite

from vector import Vector

from util import *
from timer import Timer, TimerDict, TimerDual
import maze as mz
import application as app
import play as pl

 
class Player(Sprite):
    """Class for the Player, handling Pac Man's controls, movement, and other operations."""
    DIR_VECTOR = {
        'up': (0, -1),
        'left': (-1, 0),
        'down': (0, 1),
        'right': (1, 0)
    }

    OPPOSITE_DIR = {
        'up': 'down',
        'left': 'right',
        'down': 'up',
        'right': 'left'
    }

    def __init__(self, maze: mz.Maze, play):
        super().__init__()
        self.maze = maze
        self.play = play
        self.rect_hitbox = pg.Rect((0, 0), (mz.Maze.TILE_SIZE, mz.Maze.TILE_SIZE))
        
        player_sprites = {
            'up': [pg.image.load(f"{gm.Game.PROJECT_DIR}/resources/sprites/pacs_up_{x}.png") for x in range(1, 3)],
            'down': [pg.image.load(f"{gm.Game.PROJECT_DIR}/resources/sprites/pacs_down_{x}.png") for x in range(1, 3)],
            'left': [pg.image.load(f"{gm.Game.PROJECT_DIR}/resources/sprites/pacs_left_{x}.png") for x in range(1, 3)],
            'right': [pg.image.load(f"{gm.Game.PROJECT_DIR}/resources/sprites/pacs_right_{x}.png") for x in range(1, 3)]
        }

        player_all_closed_sprite = pg.image.load(f"{gm.Game.PROJECT_DIR}/resources/sprites/pacs_all_closed.png")

        for v in player_sprites.values():
            v.insert(0, player_all_closed_sprite)

        self.pacman_animator = TimerDict(dict_frames=player_sprites, first_key='up')
        """The sprite animation handler."""

        self.lives = 3
        """The player's remaining lives."""

        self.tile = (1, 1)
        """The player's last \"steady\" tile."""

        self.tile_next = (2, 1)
        """The immediate tile for the player to move towards. Should be adjacent to `self.tile`."""

        self.tile_progress = 0
        """Player's progress of movement between `self.tile`` and `self.next_tile`.
        Should range 0 to 1 inclusive."""

        # Resets Pacman after death
        # Reset after death

    def on_hit(self):
        self.lives -= 1
    
    def reset(self):
        """Runs after death animation is finished."""
        # TODO: Implement reset function (for later)
        # TODO: Set new starting tile
        pass

    def draw(self):
        img = self.pacman_animator.imagerect()
        rect = img.get_rect()
        self.maze.blit_relative(img, rect)

    def update(self):
        self.draw()


