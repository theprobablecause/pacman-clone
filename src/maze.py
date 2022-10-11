import math
import pygame as pg
from pygame import Surface
from pygame import Sprite

from vector import Vector

class Maze(Sprite):
    ## TILE STATES
    # 0 = wall (the only non-traversable tile)
    # 1 = empty
    # 2 = food pellet
    # 3 = power pellet
    # 4 = ghost house entrance

    ## PIXEL DIMENSIONS
    # maze is 28x28 tiles (each tile having a state as described above)
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
        '0000002001011111101112000000'
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
        return px/3
    
    def tile2pixel(tile: Vector):
        return tile*3

    @staticmethod
    def vec2strpos(coord: Vector):
        x, y = math.floor(coord.x), math.floor(coord.y)
        x, y = math.floor(coord.x), math.floor(coord.y)
        return x + 28*y

    def __init__(self):
        self.maze = Maze.FRESH_MAZE
    
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
            # TODO: change score, counters
            self.maze[strpos] = 1
        elif state == 3: # power pellet
            # TODO: change score, counters, flee state
            self.maze[strpos] = 1

    def reset(self):
        self.maze = Maze.FRESH_MAZE

    def draw(self):
        pass

    def update(self):
        self.draw()