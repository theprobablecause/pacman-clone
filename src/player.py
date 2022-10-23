import random
import pygame as pg
from pygame.sprite import Sprite

from vector import Vector

from util import *
from timer import Timer, TimerDict, TimerDual
import maze as mz
import application as app
import play as pl
import ghost as gh

 
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
        self.rect = pg.Rect((0, 0), (mz.Maze.TILE_SIZE, mz.Maze.TILE_SIZE))

        player_sprites = {
            'up': [pg.image.load(f"{app.Application.PROJECT_DIR}/resources/sprites/pacs_up_{x}.png") for x in [1, 2, 1]],
            'down': [pg.image.load(f"{app.Application.PROJECT_DIR}/resources/sprites/pacs_down_{x}.png") for x in [1, 2, 1]],
            'left': [pg.image.load(f"{app.Application.PROJECT_DIR}/resources/sprites/pacs_left_{x}.png") for x in [1, 2, 1]],
            'right': [pg.image.load(f"{app.Application.PROJECT_DIR}/resources/sprites/pacs_right_{x}.png") for x in [1, 2, 1]]
        }

        player_all_closed_sprite = pg.image.load(f"{app.Application.PROJECT_DIR}/resources/sprites/pacs_all_closed.png")

        for v in player_sprites.values():
            v.insert(0, player_all_closed_sprite)

        self.pacman_animator = TimerDict(dict_frames=player_sprites, first_key='up', wait=48)
        """The sprite animation handler."""

        self.lives = 3
        """The player's remaining lives."""

        self.tile = (12, 17)
        """The player's last \"steady\" tile."""

        self.tile_next = (13, 17)
        """The immediate tile for the player to move towards. Should be adjacent to `self.tile`."""

        self.tile_progress = 0
        """Player's progress of movement between `self.tile`` and `self.next_tile`.
        Should range 0 to 1 inclusive."""

        self.eaten_ghost = None
        """Ghost being eaten."""

        self.facing = ''
        self.update_facing()
        self.maze.consume_tile(self.tile)

    def ghost_interact(self, ghost: gh.Ghost):
        # eaten; do nothing
        if ghost.mode in [gh.GhostMode.EATEN, gh.GhostMode.EATEN_INVISIBLE]: return

        if ghost.mode == gh.GhostMode.FRIGHTENED: # frightened
            ghost.mode = gh.GhostMode.EATEN_INVISIBLE
            self.play.play_state.pause_timer = 60
            self.play.play_state.action_pause = True
            self.play.sound.eat_ghost()
            # TODO: replace pacman's sprite with score text
        else: # hostile in all its forms
            self.hit()
        
        self.play.sound.stop_chomping()
        

    def hit(self):
        """When Pac Man is hit by a ghost."""
        pass

    def hit_dying(self):
        """Begins dying animation."""
        pass

    def hit_dead(self):
        """Animation ended; set states."""
        self.lives -= 1

    def update_facing(self):
        """Update `self.facing` based on `self.tile` and `self.tile_next`."""
        diff = (self.tile_next[0] - self.tile[0], self.tile_next[1] - self.tile[1])
        if diff == (0,0): return
        if diff[0] != 0: # horizontal movement
            self.facing = 'left' if diff[0] < 0 else 'right'
        else: # vertical movement
            self.facing = 'down' if diff[1] > 0 else 'up'
        
    def teleport(self, tile: tuple[int, int]):
        """Teleport Pac Man to a particular tile."""
        self.tile = tile
        self.tile_next = tile
        self.tile_next = self.get_facing_tile()
        self.tile_progress = 0
    
    def reset(self):
        """Runs after death animation is finished."""
        pass

    def get_facing_tile(self, direction:str=None):
        if direction == None:
            vec = Player.DIR_VECTOR[self.facing]
        else:
            vec = Player.DIR_VECTOR[direction]     
        return (self.tile_next[0] + vec[0], self.tile_next[1] + vec[1])

    def update_tile_next(self):
        """Determine the next intermediate tile to go to. Should only run when we've reached target tile (self.tile_progress >= 1)"""
        self.tile = self.tile_next
        tile_check = self.get_facing_tile()
        tile_state = self.maze.get_tile_state(Vector(*tile_check))
        if tile_state not in [-1, 0, 4]:
            self.tile_next = tile_check

    def try_set_direction(self, direction: str):
        if self.tile_progress >= 0.8:
            state = self.maze.get_tile_state(Vector(*self.get_facing_tile(direction)))
            if state not in [-1, 0, 4]:
                self.facing = direction

    def move(self):
        self.tile_progress += self.play.player_speed*app.Application.FRAME_TIME
        if self.tile_progress >= 1:
            self.tile_progress %= 1
            self.tile = [self.tile_next[0], self.tile_next[1]]
            self.maze.consume_tile(self.tile)
            self.update_tile_next()
            self.update_facing()

        current_tile = Vector(
            lerp(self.tile[0], self.tile_next[0], self.tile_progress),
            lerp(self.tile[1], self.tile_next[1], self.tile_progress)
        )
        px = mz.Maze.tile2pixelctr(current_tile)
        self.rect.center = (px.x, px.y)

    def draw(self):
        self.pacman_animator.key = self.facing
        img = self.pacman_animator.imagerect()

        r = img.get_rect()
        r.center = self.rect.center
        self.maze.blit_relative(img, r)

    def update(self):
        self.move()


