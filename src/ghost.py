import pygame as pg
from pygame.sprite import Sprite

from timer import Timer, TimerDict
from maze import Maze
from game import Game

class Ghost(Sprite):
    def __init__(self, type, maze: Maze):
        self.image: pg.Surface
        self.rect: pg.Rect = self.image.get_rect()
        self.rect_hitbox:pg.Rect = self.image.get_rect()
        self.rect_hitbox.size = (Maze.TILE_SIZE, Maze.TILE_SIZE)

        normal_sprites = {
            'up': [f"{Game.PROJECT_DIR}/resources/sprites/{type}_up_{x}.png" for x in range(3, 5)],
            'down': [f"{Game.PROJECT_DIR}/resources/sprites/{type}_down_{x}.png" for x in range(3, 5)],
            'left': [f"{Game.PROJECT_DIR}/resources/sprites/{type}_left_{x}.png" for x in range(3, 5)],
            'right': [f"{Game.PROJECT_DIR}/resources/sprites/{type}_right_{x}.png" for x in range(3, 5)]
        }
        self.normal_animator = TimerDict(dict_frames=normal_sprites, first_key='up')
    
    # OVERRIDE: unique AI for each ghost
    def move(self):
        pass

    def draw(self):
        pass

    def update(self):
        # TODO: determine next tile (by target), move to next position
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