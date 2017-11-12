"""
    A simple Game to test neural networks , machine learning etc

    Copyright (C) 2017  Tiago Martins

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import pygame
from settings import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        # Pass a game instance of Game Class for player to has access of the Game vars/funcs etc
        self.game = game
        self.image = pygame.image.load(PLAYER_IMAGE_LIST_RIGHT[1])
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        # Use 2 counter vars to know what image use
        self.counter_right = 0
        self.counter_left = 0
        # direc var is use for set the player direction when it is stopped
        self.direc = "right"

    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        hits_base = pygame.sprite.spritecollide(self, self.game.base, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20
        elif hits_base:
            self.vel.y = -20


    def update(self):
        # Update Sprites on the screen
        self.acc = vec(0, PLAYER_GRAV)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            # Verify if is the last image of the sprite animation, if it was restart the counter
            if self.counter_left == 2:
                self.counter_left = 0
            self.image = pygame.image.load(PLAYER_IMAGE_LIST_LEFT[self.counter_left]).convert_alpha()
            self.acc.x = -PLAYER_ACC
            self.counter_left += 1
            self.direc = 'left'

        if keys[pygame.K_RIGHT]:
            # Verify if is the last image of the sprite animation, if it was restart the counter
            if self.counter_right == 2:
                self.counter_right = 0
            self.image = pygame.image.load(PLAYER_IMAGE_LIST_RIGHT[self.counter_right]).convert_alpha()
            self.acc.x = PLAYER_ACC
            self.counter_right += 1
            self.direc = 'right'

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        # Set the Player Sprite Animation Stopped
        if self.vel.x == 0:
            if self.direc == 'left':
                self.image = pygame.image.load(PLAYER_IMAGE_LIST_LEFT[1])
            elif self.direc == 'right':
                self.image = pygame.image.load(PLAYER_IMAGE_LIST_RIGHT[1])


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image = pygame.image.load(PLATFORMS[0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Base(pygame.sprite.Sprite):
    def __init__(self,image_file,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, 71))
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
