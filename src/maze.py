import math
import pygame as pg
from pygame import Surface
from pygame.sprite import Sprite

from vector import Vector
import game as gm

class Maze(Sprite):
    ## TILE STATES
    # 0 = wall (the only non-traversable tile)
    # 1 = empty
    # 2 = food pellet
    # 3 = power pellet
    # 4 = ghost house entrance

    ## PIXEL DIMENSIONS
    # maze is 28x31 tiles (each tile having a state as described above)
    # each tile is 3*(8x8) = 24x24 pixels

    FRESH_MAZE = (
        '0000000000000000000000000000'
        '0222222222222002222222222220'
        '0200002000002002000002000020'
        '0300002000002002000002000030'
        '0200002000002002000002000020'
        '0222222222222222222222222220'
        '0200002002000000002002000020'
        '0200002002000000002002000020'
        '0222222002222002222002222220'
        '0000002000001001000002000000'
        '0000002000001001000002000000'
        '0000002001111111111002000000'
        '0000002001000440001002000000'
        '0000002001011111101002000000'
        '1111112111011111101112111111'
        '0000002001011111101002000000'
        '0000002001000000001002000000'
        '0000002001111111111002000000'
        '0000002001000000001002000000'
        '0000002001000000001002000000'
        '0222222222222002222222222220'
        '0200002000002002000002000020'
        '0200002000002002000002000020'
        '0322002222222112222222002230'
        '0002002002000000002002002000'
        '0002002002000000002002002000'
        '0222222002222002222002222220'
        '0200000000002002000000000020'
        '0200000000002002000000000020'
        '0222222222222222222222222220'
        '0000000000000000000000000000'
    )

    @staticmethod
    def pixel2tile(px: Vector):
        return px/24
    
    @staticmethod
    def tile2pixel(tile: Vector):
        return tile*24
    
    @staticmethod
    def tile2pixelctr(tile: Vector):
        return tile*24 + Vector(12, 12)

    @staticmethod
    def vec2strpos(coord: Vector):
        x, y = math.floor(coord.x), math.floor(coord.y)
        x, y = math.floor(coord.x), math.floor(coord.y)
        return x + 28*y

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.maze = Maze.FRESH_MAZE
        self.image = pg.image.load(gm.Game.PROJECT_DIR + '/resources/sprites/maze.png')
        self.rect = self.image.get_rect()
        self.object_imgs = {
            2: pg.image.load(gm.Game.PROJECT_DIR + '/resources/sprites/food_pellet.png'),
            3: pg.image.load(gm.Game.PROJECT_DIR + '/resources/sprites/power_food.png')
        }
    
    def get_tile_state(self, vec: Vector):
        strpos = Maze.vec2strpos(vec)
        return int(self.maze[strpos])
    
    # change tile state, set other game states
    def consume_tile(self, vec: Vector):
        state = self.get_tile_state(vec)
        strpos = Maze.vec2strpos(vec)

        if state == 0: # (why are we eating a wall?)
            raise ValueError('tried to consume a wall!')
        elif state == 2: # food pellet
            self.maze[strpos] = 1
            # TODO: change score, counters
        elif state == 3: # power pellet
            self.maze[strpos] = 1
            # TODO: change score, counters, flee state

    def reset(self):
        self.maze = Maze.FRESH_MAZE

    def draw(self):
        # draw maze
        rect = self.rect
        rect.center = self.screen.get_rect().center
        self.screen.blit(self.image, rect)
        # TODO: draw objects currently in maze (ie. food pellets)

    def update(self):
        self.draw()