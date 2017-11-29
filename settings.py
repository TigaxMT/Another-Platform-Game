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

import random
import pygame

TITLE = "Another Platform Game"
WIDTH = 800
HEIGHT = 600
FPS = 60

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8

# The platform png is 195x71

PLATFORM_LIST = [(0, HEIGHT - 71, 195, 71)] # This platform is the base platform

# Load audio

MUSIC = ["audio/Game_Music.mp3"]

#Images for Sprite Animation

PLAYER_IMAGE_LIST_LEFT = ["sprites/Run_left (1).png","sprites/Run_left (2).png","sprites/Run_left (3).png",
                          "sprites/Run_left (4).png","sprites/Run_left (5).png","sprites/Run_left (6).png",
                          "sprites/Run_left (7).png","sprites/Run_left (8).png"]

PLAYER_IMAGE_LIST_RIGHT = ["sprites/Run_right (1).png","sprites/Run_right (2).png","sprites/Run_right (3).png",
                           "sprites/Run_right (4).png","sprites/Run_right (5).png","sprites/Run_right (6).png",
                           "sprites/Run_right (7).png","sprites/Run_right (8).png"]

PLAYER_IMAGE_STOPPED = ["sprites/Idle (1).png","sprites/Idle (2).png","sprites/Idle (3).png",
                        "sprites/Idle (4).png","sprites/Idle (5).png","sprites/Idle (6).png",
                        "sprites/Idle (7).png","sprites/Idle (8).png","sprites/Idle (9).png",
                        "sprites/Idle (10).png"]

BG = ["sprites/BG.png"]
PLATFORMS = ["sprites/platform.png"]
ASSETS = ["sprites/Bush (1).png","sprites/Bush (2).png","sprites/Bush (3).png","sprites/Bush (4).png",
          "sprites/Mushroom_1.png","sprites/Mushroom_2.png","sprites/Stone.png","sprites/Tree_2.png",
          "sprites/Tree_3.png", "sprites/Sign_2.png"]
BASE = ["sprites/base.png"]

# Credits

CREDITS = ["Programmers: Tiago Martins", "Kelvin Ferreira","Sounds: Bruna Silva (Girlfriend of Tiago Martins)","Designers: Zuhria Alfitra","Tiago Martins"]

SAMPLE = ["sprites/sample.png"]

# define colors

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)
YELLOW = pygame.Color(255, 255, 0)
LIGHTBLUE = pygame.Color(0, 155, 155)
BRIGHT_RED = pygame.Color(255,98,98)
BRIGHT_GREEN = pygame.Color(73,253,79)
DARK_YELLOW = pygame.Color(255,153,51)
