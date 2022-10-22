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
    """Base class for the Player. Should not be instantiated!"""
    def __init__(self, type, tile_home, maze: mz.Maze, play):
        super().__init__()
        self.maze = maze
        self.play = play
        self.rect_hitbox = pg.Rect((0, 0), (mz.Maze.TILE_SIZE, mz.Maze.TILE_SIZE))

        self.tile = (1, 1)
        """The ghost's last \"steady\" tile."""

        self.tile_next = (2, 1)
        """The immediate tile for the ghost to move towards. Should be adjacent to `self.tile`."""

        self.tile_progress = 0
        """PLayer's progress of movement between `self.tile`` and `self.next_tile`.
        Should range 0 to 1 inclusive."""

        # Resets Pacman after death
        # Reset after death
    def reset():
        global game
        app.ghosts = [Ghost(14.0, 13.5, "red", 0), Ghost(17.0, 11.5, "blue", 1), Ghost(17.0, 13.5, "pink", 2), Ghost(17.0, 15.5, "orange", 3)]
        for ghost in app.ghosts:
            ghost.setTarget()
        app.pacman = Pacman(26.0, 13.5)
        app.lives -= 1
        app.paused = True
        app.draw()

'''DIR_VECTOR = {
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

class Player(Sprite):
    """Base class for the Player. Should not be instantiated!"""
    # Draws Pacman
    self.pacman.draw()
    pygame.display.update()

    def __init__(self, type, tile_home, maze: mz.Maze, play):
        super().__init__()
        self.maze = maze
        self.play = play
        self.rect_hitbox = pg.Rect((0, 0), (mz.Maze.TILE_SIZE, mz.Maze.TILE_SIZE))

        self.tile = (1, 1)
        """The ghost's last \"steady\" tile."""

        self.tile_next = (2, 1)
        """The immediate tile for the ghost to move towards. Should be adjacent to `self.tile`."""

        self.tile_progress = 0
        """PLayer's progress of movement between `self.tile`` and `self.next_tile`.
        Should range 0 to 1 inclusive."""

        # Resets Pacman after death
        # Reset after death
    def reset():
        global game
        game.ghosts = [Ghost(14.0, 13.5, "red", 0), Ghost(17.0, 11.5, "blue", 1), Ghost(17.0, 13.5, "pink", 2), Ghost(17.0, 15.5, "orange", 3)]
        for ghost in game.ghosts:
            ghost.setTarget()
        game.pacman = Pacman(26.0, 13.5)
        game.lives -= 1
        game.paused = True
        game.draw()

        ## SPRITES ##
        normal_sprites = {
            'up': [pg.image.load(f"{gm.Game.PROJECT_DIR}/resources/sprites/{type}_up_{x}.png") for x in range(3, 5)],
            'down': [pg.image.load(f"{gm.Game.PROJECT_DIR}/resources/sprites/{type}_down_{x}.png") for x in range(3, 5)],
            'left': [pg.image.load(f"{gm.Game.PROJECT_DIR}/resources/sprites/{type}_left_{x}.png") for x in range(3, 5)],
            'right': [pg.image.load(f"{gm.Game.PROJECT_DIR}/resources/sprites/{type}_right_{x}.png") for x in range(3, 5)]
        }

        self.image = self.normal_animator.imagerect()
        self.update_facing()

        # If Pacman hits a wall, continuous movement will stop
        def checkInput(p):
            global joyin, joystick_count
            xaxis = yaxis = 0
            if joystick_count > 0:
                xaxis = joyin.get_axis(0)
                yaxis = joyin.get_axis(1)
            if key.get_pressed()[K_LEFT] or xaxis < -0.8:
                p.angle = 180
                p.movex = -20
            if key.get_pressed()[K_RIGHT] or xaxis > 0.8:
                p.angle = 0
                p.movex = 20
            if key.get_pressed()[K_UP] or yaxis < -0.8:
                p.angle = 90
                p.movey = -20
            if key.get_pressed()[K_DOWN] or yaxis > 0.8:
                p.angle = 270
                p.movey = 20

        # inside update() function

            if player.movex or player.movey:
                inputLock()
                animate(player, pos=(player.x + player.movex, player.y + player.movey), duration=1/SPEED, tween='linear', on_finished=inputUnLock)

        # outside update() function

        def inputLock():
            global player
            player.inputActive = False

        def inputUnLock():
            global player
            player.movex = player.movey = 0
            player.inputActive = True

    def update_facing(self):
        """Update `self.facing` based on `self.tile` and `self.tile_next`."""
        diff = (self.tile_next[0] - self.tile[0], self.tile_next[1] - self.tile[1])
        if diff[0] != 0: # horizontal movement
            self.facing = 'left' if diff[0] < 0 else 'right'
        else: # vertical movement
            self.facing = 'down' if diff[1] > 0 else 'up'

    # Calling method from maze to consume tile once destination tile is reached
    maze.consume_tile()'''

""" import pygame
from pygame.sprite import Sprite

class Character(Sprite):
    def __init__(self, sheet_location, pos, screen, map):
        super(Character, self).__init__()
        self.sheet = pygame.image.load(sheet_location).convert_alpha()
        self.pos = pos
        self.rect = pygame.Rect(pos[0], pos[1], 28, 28)
        self.velocity = (1, 0)
        self.old_velocity = (0, 0)
        self.still_wall = False
        self.screen = screen
        self.speed_counter = 0
        self.map = map

    def strip_from_sheet(self, start, size, columns, rows):
        frames = []
        for j in range(rows):
            for i in range(columns):
                location = (start[0] + size[0] * i, start[1] + size[1] * j)
                frames.append(self.sheet.subsurface(pygame.Rect(location, size)))
        return frames

    def set_image(self, image):
        self.image = image

    def change_direction(self, direction, pacman_timer):
        if direction == 'r':
            self.velocity = (1, 0)
        elif direction == 'l':
            self.velocity = (-1, 0)
        elif direction == 'u':
            self.velocity = (0, -1)
        elif direction == 'd':
            self.velocity = (0, 1)
        pacman_timer.frameindex = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update_movement(self, collision):
        if self.speed_counter == 3:
            # print(self.map_pos)
            # if self.velocity == (1, 0) and self.map[self.map_pos[0]][self.map_pos[1] + 1] == 'x':
            #     self.velocity = (0, 0)
            # elif self.velocity == (-1, 0) and self.map[self.map_pos[0]][self.map_pos[1] - 1] == 'x':
            #     self.velocity = (0, 0)
            # elif self.velocity == (0, 1) and self.map[self.map_pos[0] - 1][self.map_pos[1]] == 'x':
            #     self.velocity = (0, 0)
            # elif self.velocity == (0, -1) and self.map[self.map_pos[0] + 1][self.map_pos[1]] == 'x':
            #     self.velocity = (0, 0)
            #
            # if self.rect.x >= self.next_pos[0]:
            #     self.map_pos = (self.map_pos[0], self.map_pos[1] + 1)
            #     self.next_pos = (self.rect.centerx + 34, self.rect.centery + 34)
            # elif self.rect.x <= self.next_pos[0] - 68:
            #     self.map_pos = (self.map_pos[0], self.map_pos[1] - 1)
            #     self.next_pos = (self.rect.centerx + 34, self.rect.centery + 34)
            # elif self.rect.y >= self.next_pos[1]:
            #     self.map_pos = (self.map_pos[0] - 1, self.map_pos[1])
            #     self.next_pos = (self.rect.centerx + 34, self.rect.centery + 34)
            # elif self.rect.y <= self.next_pos[1] - 68:
            #     self.map_pos = (self.map_pos[0] + 1, self.map_pos[1])
            #     self.next_pos = (self.rect.centerx + 34, self.rect.centery + 34)
            if collision is None:
                self.still_wall = False
                self.rect.x += self.velocity[0]
                self.rect.y += self.velocity[1]
            else:
                if self.still_wall:
                    self.rect.x -= self.old_velocity[0]
                    self.rect.y -= self.old_velocity[1]
                else:
                    self.rect.x -= self.velocity[0]
                    self.rect.y -= self.velocity[1]
                self.old_velocity = self.velocity
                self.still_wall = True
                self.velocity = (0, 0)
            self.speed_counter = 0
        else:
            self.speed """