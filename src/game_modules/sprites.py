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

import time
import pygame
import random

#settings
from game_modules.settings.colors import GameColors
from game_modules.settings.sprites import PlayerSprites, PlatformSprites

from game_modules.settings.platform import PlatformSettings
from game_modules.settings.player import PlayerSettings

vec = pygame.math.Vector2  # define a variable vectors for the movements


class Player(pygame.sprite.Sprite):  # Creates a Player Sprite
    def __init__(self, game):

        #Initialize the Sprite function
        pygame.sprite.Sprite.__init__(self)

        # Pass a game instance of Game Class for player to has access of the Game vars/funcs etc
        self.game = game

        #Define the stop player sprite and get the rectangle of him
        self.image = pygame.image.load(
            PlayerSprites.PLAYER_IMAGE_LIST_RIGHT[1])
        self.rect = self.image.get_rect()
        self.rect.center = (PlatformSettings.WIDTH / 2,
                            PlatformSettings.HEIGHT / 2)

        #Define the vectors of position , velocity and acceleration
        self.pos = vec(PlatformSettings.WIDTH / 2,
                       PlatformSettings.HEIGHT - 71)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        # Use 3 counter variables to know what image use
        self.counter_right = 0
        self.counter_left = 0
        self.counter_stopped = 0

        # direc variable is use for set the player direction when it is stopped
        self.direc = "right"

    def kill_move(self,entity):

        if entity == "Plaform":

            #Moving each platform and kill platforms reach Width 0
            for plat in self.game.platforms:
                if self.vel.x > 0:
                    plat.rect.x -= abs(self.vel.x)
                if plat.rect.right < 0:
                    plat.kill()

        elif entity == "Asset":

            #Moving each asset and kill assets reach Width 0
            for ass in self.game.assets:
                if self.vel.x > 0:
                    ass.rect.x -= abs(self.vel.x)
                if ass.rect.right < 0:
                    ass.kill()

        elif entity == "Base":

            #Moving each base and kill bases reach Width 0
            for bases in self.game.base:
                if self.vel.x > 0:
                    bases.rect.x -= abs(self.vel.x)
                if bases.rect.right < 0:
                    bases.kill()

            #Randomize base platforms,only if don't have 2 bases spawned
            while len(self.game.base) < 2:
                if bases.rect.right <= PlatformSettings.WIDTH:
                    base = Base(PlatformSprites.BASE[0], random.randrange(
                        PlatformSettings.WIDTH, PlatformSettings.WIDTH + 50),
                        PlatformSettings.HEIGHT - 71)
                    self.game.base.add(base)
                    self.game.all_sprites.add(base)

    def jump(self):  # jump only if standing on a platform

        #Increment the player rectangle position for a better collision detection
        self.rect.x += 1

        #Verify if player hits a platform or a base
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        hits_base = pygame.sprite.spritecollide(self, self.game.base, False)

        #Decrement the player rectangle position for the initial position

        #If it stand in a platform or a base, the y velocity is decremented
        self.rect.x -= 1
        if hits:
            self.vel.y = -20
        elif hits_base:
            self.vel.y = -20

    def update(self):  # Update Sprites on the screen

        #Define acceleration with the gravity constant (defined in settings script)
        self.acc = vec(0, PlayerSettings.PLAYER_GRAV)

        #Store all the keys pressed
        keys = pygame.key.get_pressed()

        #If left key pressed
        if keys[pygame.K_LEFT]:

            # Verify if is the last image of the sprite animation, if it was restart the counter
            if self.counter_left == 7:
                self.counter_left = 0

            #Update the player image with the correct image, to give the sensation of movement
            self.image = pygame.image.load(
                PlayerSprites.PLAYER_IMAGE_LIST_LEFT[self.counter_left]).convert_alpha()

            #Put an negative(oposite for the right movement) constant acceleration to the player to give better physics
            self.acc.x = -PlayerSettings.PLAYER_ACC

            self.counter_left += 1
            self.direc = 'left'

        #If right key pressed
        if keys[pygame.K_RIGHT]:
            # Verify if is the last image of the sprite animation, if it was restart the counter
            if self.counter_right == 7:
                self.counter_right = 0

            #Update the player image with the correct image, to give the sensation of movement
            self.image = pygame.image.load(
                PlayerSprites.PLAYER_IMAGE_LIST_RIGHT[self.counter_right]).convert_alpha()

            #Put an positive(oposite for the left movement) constant acceleration to the player to give better physics
            self.acc.x = PlayerSettings.PLAYER_ACC

            self.counter_right += 1
            self.direc = 'right'

        # apply friction to the acceleration
        self.acc.x += self.vel.x * PlayerSettings.PLAYER_FRICTION

        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

        # Set the Player Sprite Animation Stopped
        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            if self.counter_stopped == 9:
                self.counter_stopped = 0

            self.image = pygame.image.load(
                PlayerSprites.PLAYER_IMAGE_STOPPED[self.counter_stopped])
            self.counter_stopped += 1
        else:
            counter_stopped = 0


class Asset(pygame.sprite.Sprite):  # Creates a Asset Sprite
    def __init__(self, image_file, x, y):

        #Initialize the Sprite function
        pygame.sprite.Sprite.__init__(self)

        #Load the image file and get the rectangle of him
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()

        #Put the rectangle in the position
        self.rect.x = x
        self.rect.y = y


class Platform(pygame.sprite.Sprite):  # Creates a Platform Sprite
    def __init__(self, x, y, w, h):

        #Initialize the Sprite function
        pygame.sprite.Sprite.__init__(self)

        #Create the surface to the image
        self.image = pygame.Surface((w, h))

        #Load the image and get the rectangle of him
        self.image = pygame.image.load(
            PlatformSprites.PLATFORMS[0]).convert_alpha()
        self.rect = self.image.get_rect()

        #Put the rectangle in the position
        self.rect.x = x
        self.rect.y = y


class Base(pygame.sprite.Sprite):  # Creates a Base Sprite
    def __init__(self, image_file, x, y):

        #Initialize the Sprite function
        pygame.sprite.Sprite.__init__(self)

        #Create the surface to the image
        self.image = pygame.Surface((PlatformSettings.WIDTH, 71))

        #Load the image and get the rectangle of him
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()

        #Put the rectangle in the position
        self.rect.x = x
        self.rect.y = y


class Background(pygame.sprite.Sprite):  # Creates a Background Sprite
    def __init__(self, image_file, location):

        #Initialize the Sprite function
        pygame.sprite.Sprite.__init__(self)

        #Load the image file and get the rectangle of him
        self.image = pygame.image.load(image_file).convert_alpha()

        #Put the rectangle in the position
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
