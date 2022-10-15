import pygame
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
            self.speed