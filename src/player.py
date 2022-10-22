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

    def __init__(self, maze: mz.Maze, play):
        super().__init__()
        self.maze = maze
        self.play = play
        self.rect_hitbox = pg.Rect((0, 0), (mz.Maze.TILE_SIZE, mz.Maze.TILE_SIZE))

        player_sprites = {
            'up': [pg.image.load(f"{app.Application.PROJECT_DIR}/resources/sprites/pacs_up_{x}.png") for x in range(1, 3)],
            'down': [pg.image.load(f"{app.Application.PROJECT_DIR}/resources/sprites/pacs_down_{x}.png") for x in range(1, 3)],
            'left': [pg.image.load(f"{app.Application.PROJECT_DIR}/resources/sprites/pacs_left_{x}.png") for x in range(1, 3)],
            'right': [pg.image.load(f"{app.Application.PROJECT_DIR}/resources/sprites/pacs_right_{x}.png") for x in range(1, 3)]
        }

        player_all_closed_sprite = pg.image.load(f"{app.Application.PROJECT_DIR}/resources/sprites/pacs_all_closed.png")

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

        self.facing = ''
        self.update_facing()

    def on_hit(self):
        self.lives -= 1

    def update_facing(self):
        """Update `self.facing` based on `self.tile` and `self.tile_next`."""
        diff = (self.tile_next[0] - self.tile[0], self.tile_next[1] - self.tile[1])
        if diff == (0,0): return
        if diff[0] != 0: # horizontal movement
            self.facing = 'left' if diff[0] < 0 else 'right'
        else: # vertical movement
            self.facing = 'down' if diff[1] > 0 else 'up'
    
    def reset(self):
        """Runs after death animation is finished."""
        # TODO: Implement reset function (for later)
        self.maze = Maze.FRESH_MAZE
        # TODO: Set new starting tile
        self.tile
        pass

    def update_tile_next(self):
        prev = self.tile_next

        # TODO: detect wall
        for dir in candidate_dirs:
            vec = DIR_VECTOR[dir]
            check_tile = (self.tile[0]+vec[0], self.tile[1]+vec[1])
            state = self.maze.get_tile_state(Vector(check_tile[0], check_tile[1]))
            if state in [0, -1] or (self.mode != 3 and state == 4):
                # skip non-traversable, and if not in eaten
                # state, skip ghost house entrance.
                continue
            candidate_tiles[dir] = check_tile
            dist[dir] = Vector.distance_squared(Vector(*check_tile), Vector(*self.target))      

        # TODO: set self.tile_next DEPENDING ON self.facing
        self.tile_next = (prev[0]+1, prev[1])

    def move(self):
        self.tile_progress += self.play.player_speed*app.Application.FRAME_TIME
        if self.tile_progress >= 1:
            self.maze.consume_tile(self.tile)
            self.tile_progress %= 1
            self.tile = [self.tile_next[0], self.tile_next[1]]
            self.maze.consume_tile(self.tile)
            self.update_tile_next()
            self.update_facing()

    def draw(self):
        self.pacman_animator.key = self.facing
        img = self.pacman_animator.imagerect()
        # coordinates
        current_tile = Vector(
            lerp(self.tile[0], self.tile_next[0], self.tile_progress),
            lerp(self.tile[1], self.tile_next[1], self.tile_progress)
        )
        px = mz.Maze.tile2pixelctr(current_tile)
        r = img.get_rect()
        r.center = (px.x, px.y)
        self.maze.blit_relative(img, r)

    def update(self):
        self.move()
        self.draw()


