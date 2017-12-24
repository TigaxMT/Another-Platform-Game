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


"""
    Constants for sprite animation
"""

class PlayerSprites:
    """
        Player sprites
    """
    PLAYER_IMAGE_LIST_LEFT = [
        "sprites/Run_left (%i).png" % i for i in range(1, 10)]
    PLAYER_IMAGE_LIST_RIGHT = [
        "sprites/Run_right (%i).png" % i for i in range(1, 10)]
    PLAYER_IMAGE_STOPPED = ["sprites/Idle (%i).png" % i for i in range(1, 10)]


class PlatformSprites:
    """
        Enviroment sprites
    """
    BACKGROUND = ["sprites/BG.png"]
    PLATFORMS = ["sprites/platform.png"]
    ASSETS = [
        "sprites/Bush (1).png", "sprites/Bush (2).png", "sprites/Bush (3).png",
        "sprites/Bush (4).png", "sprites/Mushroom_1.png", "sprites/Mushroom_2.png",
        "sprites/Stone.png", "sprites/Tree_2.png", "sprites/Tree_3.png", "sprites/Sign_2.png"]
    BASE = ["sprites/base.png"]
    SAMPLE = ["sprites/sample.png"]

class EnemySprites:
    """
        Enemy sprites
    """
    ENEMY_IMAGE_LIST_LEFT = [
        "sprites/Run_left (%i).png" % i for i in range(1, 10)]
    ENEMY_IMAGE_LIST_RIGHT = [
        "sprites/Run_right (%i).png" % i for i in range(1, 10)]
    ENEMY_IMAGE_STOPPED = ["sprites/Idle (%i).png" % i for i in range(1, 10)]