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


# Widgets
import pygame
from game_modules.settings.colors import GameColors


class Widgets:
    """
        Widgets is responsible to show interactable objects on screen
    """

    def __init__(self, surface):  # Define the surface screen
        self.surface = surface

        #Define and initialize with random data the variable to manipulate and Draw Text Objects
        self.smallText = pygame.font.SysFont(None, 20)
        self.textSurf, self.textRect = self.text_objects(
            "Initialize with Random data", self.smallText, GameColors.BLACK)
    
    @classmethod
    def text_objects(self, text, font, color=GameColors.BLACK):

        # Creates Text Messages
        textSurface = font.render(text, True, color)

        #Return the surface and rectangle
        return textSurface, textSurface.get_rect()

    def button(self, msg, x, y, w, h, ic, ac, action=None):  # Create Buttons
        pygame.init()
        #Store all the clicks and the positions of mouse
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #If the mouse is at the top or not of the button change the color button
        if x + w > mouse[0] > x and y + h > mouse[1] > y:

            #Change to a bright color button
            pygame.draw.rect(self.surface, ac, (x, y, w, h))

            #Create and draw a surface and rectangle for the Message text
            self.smallText = pygame.font.SysFont(None, 20)
            self.textSurf, self.textRect = self.text_objects(
                msg, self.smallText, GameColors.BLACK)
            self.textRect.center = ((x + (w / 2)), (y + (h / 2)))
            self.surface.blit(self.textSurf, self.textRect)

            #If the button is clicked and if the action parameter is not none,
            #so call the action passed
            if click[0] == 1 and action != None:
                action()
        else:

            #Change to a darker color button
            pygame.draw.rect(self.surface, ic, (x, y, w, h))

            #Create and draw a surface and rectangle for the Message text
            self.smallText = pygame.font.SysFont(None, 20)
            self.textSurf, self.textRect = self.text_objects(
                msg, self.smallText, GameColors.BLACK)
            self.textRect.center = ((x + (w / 2)), (y + (h / 2)))
            self.surface.blit(self.textSurf, self.textRect)
