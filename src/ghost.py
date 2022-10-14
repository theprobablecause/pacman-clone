import pygame as pg
from pygame.sprite import Sprite

from vector import Vector

from util import *
from timer import TimerDict
import maze as mz
import game as gm
import play as pl

class Ghost(Sprite):
    """Base class for the ghost. Should not be instantiated!"""
    def __init__(self, type, maze: mz.Maze, play):
        self.maze = maze
        self.play = play
        self.rect_hitbox = pg.Rect((0, 0), (mz.Maze.TILE_SIZE, mz.Maze.TILE_SIZE))

        self.tile = [1, 1]
        """The ghost's last \"steady\" tile."""

        self.next_tile = [2, 1]
        """The immediate tile for the ghost to move towards. Should be adjacent to `self.tile`."""

        self.target = (0, 0)
        """The tile that the ghost will ultimately be working towards."""

        self.tile_progress = 0
        """Ghost's progress of movement between `self.tile`` and `self.next_tile`.
        Should range 0 to 1 inclusive."""

        self.facing = ''
        """Which way the ghost is currently facing."""

        self.mode = 0
        """The ghost's current behavior mode.
        
        Possible modes:
        0: Scatter
        1: Chase
        2: Frightened
        3: Eaten"""

        ## SPRITES ##
        normal_sprites = {
            'up': [pg.image.load(f"{gm.Game.PROJECT_DIR}/resources/sprites/{type}_up_{x}.png") for x in range(3, 5)],
            'down': [pg.image.load(f"{gm.Game.PROJECT_DIR}/resources/sprites/{type}_down_{x}.png") for x in range(3, 5)],
            'left': [pg.image.load(f"{gm.Game.PROJECT_DIR}/resources/sprites/{type}_left_{x}.png") for x in range(3, 5)],
            'right': [pg.image.load(f"{gm.Game.PROJECT_DIR}/resources/sprites/{type}_right_{x}.png") for x in range(3, 5)]
        }
        
        self.normal_animator = TimerDict(dict_frames=normal_sprites, first_key='up')
        """The sprite animation handler for normal mode."""

        self.image = self.normal_animator.imagerect()

    def update_target(self) -> None:
        """OVERRIDE: Set the next target tile. Should only modify `self.target`!"""
        pass
    
    def move(self):
        """Move towards target tile.
        If `self.tile_progress` is 1 after moving, update our target with `self.update_target()`.
        Also updates `self.facing` and `self.next_tile`."""

        # When next_tile is reached, update target and next_tile
        if self.tile_progress >= 1:
            self.tile_progress = 0
            self.update_target()
            self.tile = [self.next_tile[0], self.next_tile[1]]
            # TODO: calculate next_tile properly
            self.next_tile[0] += 1
        
        # Move towards next_tile
        next_progress = self.tile_progress + self.play.ghosts_speed*gm.Game.FRAME_TIME
        self.tile_progress = clip(next_progress, 0, 1) # may not require?

        # Face direction calculation
        diff = (self.next_tile[0] - self.tile[0], self.next_tile[1] - self.tile[1])
        if diff[0] != 0: # horizontal movement
            self.facing = 'left' if diff[0] < 0 else 'right'
        else: # vertical movement
            self.facing = 'down' if diff[1] < 0 else 'up'
    
    def flip(self):
        """Flip our movement completely."""
        pass

    def draw(self):
        # coordinates
        current_tile = Vector(
            lerp(self.tile[0], self.next_tile[0], self.tile_progress),
            lerp(self.tile[1], self.next_tile[1], self.tile_progress)
        )
        px = mz.Maze.tile2pixelctr(current_tile)
        # graphic retrieval
        self.normal_animator.key = self.facing
        self.image = self.normal_animator.imagerect()
        r = self.image.get_rect()
        r.center = (px.x, px.y)

        self.maze.blit_relative(self.image, r)

    def update(self):
        self.move()
        self.draw()

class Blinky(Ghost):
    def __init__(self, maze):
        super().__init__(type='', maze=maze)
    
    def move(self):
        pass

class Pinky(Ghost):
    def __init__(self, maze):
        super().__init__(type='', maze=maze)
    
    def move(self):
        pass

class Inky(Ghost):
    def __init__(self, maze):
        super().__init__(type='', maze=maze)
    
    def move(self):
        pass

class Clyde(Ghost):
    def __init__(self, maze):
        super().__init__(type='', maze=maze)
    
    def move(self):
        pass