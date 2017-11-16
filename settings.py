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

# game options/settings
import random

TITLE = "Another Platform Game"
WIDTH = 800
HEIGHT = 600
FPS = 40

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8

# The platform png is 195x71

PLATFORM_LIST = [(0, HEIGHT - 71, 195, 71)] # This platform is the base platform

# Load audio

MUSIC = ["audio/Game_Music.mp3"]

#Images for Sprite Animation

PLAYER_IMAGE_LIST_LEFT = ["sprites/left_0.png","sprites/left_1.png","sprites/left_2.png"]
PLAYER_IMAGE_LIST_RIGHT = ["sprites/right_0.png","sprites/right_1.png","sprites/right_2.png"]
BG = ["sprites/BG.png"]
PLATFORMS = ["sprites/platform.png"]
ASSETS = ["sprites/Tree_2.png","sprites/Tree_3.png"]
BASE = ["sprites/base.png"]

# Credits

CREDITS = ["Programmers: Tiago Martins & Kelvin Ferreira","Sounds: Bruna Silva (Girlfriend of Tiago Martins)","Designers: Zuhria Alfitra a.k.a pzUH"]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BRIGHT_RED = (255,98,98)
BRIGHT_GREEN = (73,253,79)
DARK_YELLOW = (255,153,51)
