"""
    A simple platform game written in Python

    Copyright (C) 2017-2018  Tiago Martins, Kelvin Ferreira

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

from game_modules.settings.platform import PlatformSettings

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