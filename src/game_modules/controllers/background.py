"""
    A simple Game to test neural networks , machine learning etc

    Copyright (C) 2017  Tiago Martins, Kelvin Ferreira

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


class Background(pygame.sprite.Sprite):  # Creates a Background Sprite
    def __init__(self, image_file, location):

        #Initialize the Sprite function
        pygame.sprite.Sprite.__init__(self)

        #Load the image file and get the rectangle of him
        self.image = pygame.image.load(image_file).convert_alpha()

        #Put the rectangle in the position
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
