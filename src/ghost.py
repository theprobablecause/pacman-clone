import pygame as pg
from pygame.sprite import Sprite

from vector import Vector

from util import *
from timer import TimerDict
import maze as mz
import game as gm
import play as pl

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

class Ghost(Sprite):
    """Base class for the ghosts. Should not be instantiated!"""
    def __init__(self, type, tile_home, maze: mz.Maze, play):
        self.maze = maze
        self.play = play
        self.rect_hitbox = pg.Rect((0, 0), (mz.Maze.TILE_SIZE, mz.Maze.TILE_SIZE))

        self.tile = (1, 1)
        """The ghost's last \"steady\" tile."""

        self.tile_next = (2, 1)
        """The immediate tile for the ghost to move towards. Should be adjacent to `self.tile`."""

        self.tile_home = tile_home
        """The tile that the ghost will target during scatter mode."""

        self.target = tile_home
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
        3: Eaten
        4: In ghost house"""

        self.debug_draw_rect = pg.surface.Surface(size=(24, 24))
        self.debug_draw_rect.fill((255, 0, 0))

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
        self.update_facing()

    def update_target(self) -> None:
        """OVERRIDE: Set the next target tile. Should only modify `self.target`!"""
        pass

    def update_next_tile(self):
        """Sets `self.next_tile` based on `self.target`."""
        opposite_dir = OPPOSITE_DIR[self.facing]
        candidate_dirs = ['up', 'left', 'down', 'right']
        candidate_dirs.remove(opposite_dir)
        candidate_tiles = {}
        dist = {}

        # wall check
        for dir in candidate_dirs:
            vec = DIR_VECTOR[dir]
            check_tile = (self.tile[0]+vec[0], self.tile[1]+vec[1])
            candidate_tiles[dir] = check_tile
            state = self.maze.get_tile_state(Vector(check_tile[0], check_tile[1]))
            if state in [0, -1]:
                # skip non-traversable
                continue
            if self.mode != 3 and state == 4:
                # skip ghost house entrance if
                # not in eaten state
                continue
            dist[dir] = Vector.distance_squared(Vector(*check_tile), Vector(*self.target))
        if len(dist) > 0:
            dir = min(dist, key=dist.get)
        else:
            dir = opposite_dir

        self.tile_next = candidate_tiles[dir]
        # print(f'Tiles: {candidate_tiles}')
        # print(f'Dist: {dist}')
        # print(self.facing + '\n')
    
    def update_facing(self):
        """Update `self.facing` based on `self.tile` and `self.next_tile`."""
        diff = (self.tile_next[0] - self.tile[0], self.tile_next[1] - self.tile[1])
        if diff[0] != 0: # horizontal movement
            self.facing = 'left' if diff[0] < 0 else 'right'
        else: # vertical movement
            self.facing = 'down' if diff[1] > 0 else 'up'

    def move(self):
        """Move towards target tile.
        If `self.tile_progress` is 1 after moving, update our target with `self.update_target()`.
        Also updates `self.facing` and `self.next_tile`."""

        # When next_tile is reached, update target and next_tile
        if self.tile_progress >= 1:
            self.tile_progress %= 1
            self.tile = [self.tile_next[0], self.tile_next[1]]

            if self.mode == 0:
                # scatter
                self.target = self.tile_home
            elif self.mode == 1:
                # chase
                self.update_target()

            self.update_next_tile()
            self.update_facing()
        
        # Move towards next_tile
        self.tile_progress += self.play.ghosts_speed*gm.Game.FRAME_TIME
    
    def flip(self):
        """Flip our movement completely."""
        pass

    def draw(self):
        # coordinates
        current_tile = Vector(
            lerp(self.tile[0], self.tile_next[0], self.tile_progress),
            lerp(self.tile[1], self.tile_next[1], self.tile_progress)
        )
        px = mz.Maze.tile2pixelctr(current_tile)
        # graphic retrieval
        self.normal_animator.key = self.facing
        self.image = self.normal_animator.imagerect()
        r = self.image.get_rect()
        r.center = (px.x, px.y)

        self.maze.blit_relative(self.image, r)

        target_vec = mz.Maze.tile2pixelctr(Vector(*self.target))
        target_pt = (target_vec.x, target_vec.y)
        target_rect = pg.Rect((0, 0), (24, 24))
        target_rect.center = target_pt
        self.maze.blit_relative(self.debug_draw_rect, target_rect)

    def update(self):
        self.move()
        self.draw()

class Blinky(Ghost):
    def __init__(self, maze, play):
        super().__init__(type='reds', tile_home=(25, -4), maze=maze, play=play)
    
    def update_target(self):
        pass

class Pinky(Ghost):
    def __init__(self, maze):
        super().__init__(type='', maze=maze)
    
    def update_target(self):
        pass

class Inky(Ghost):
    def __init__(self, maze):
        super().__init__(type='', maze=maze)
    
    def update_target(self):
        pass

class Clyde(Ghost):
    def __init__(self, maze):
        super().__init__(type='', maze=maze)
    
    def update_target(self):
        pass