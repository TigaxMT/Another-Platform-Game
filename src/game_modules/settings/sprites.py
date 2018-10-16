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


"""
    Constants for sprite animation
"""

class PlayerSprites:
    """
        Player sprites
    """
    PLAYER_IMAGE_LIST_LEFT = [
        "sprites/Player/Run_left (%i).png" % i for i in range(1, 10)]

    PLAYER_IMAGE_LIST_RIGHT = [
        "sprites/Player/Run_right (%i).png" % i for i in range(1, 10)]

    PLAYER_IMAGE_STOPPED = ["sprites/Player/Idle (%i).png" % i for i in range(1, 10)]
    
    PLAYER_IMAGE_DEAD = ["sprites/Player/Dead (%i).png" % i for i in range(0, 9)]
    
    PLAYER_IMAGE_BACKFLIP = ["sprites/Player/BackFlip (%i).png" % i for i in range(0, 9)]

    PLAYER_IMAGE_ATTACK_RIGHT = ["sprites/Player/Attack_Right (%i).png" % i for i in range(0, 9)]

    PLAYER_IMAGE_ATTACK_LEFT = ["sprites/Player/Attack_Left (%i).png" % i for i in range(0, 9)]

class PlatformSprites:
    """
        Enviroment sprites
    """
    BACKGROUND = ["sprites/Backgrounds/BG.png"]
    PLATFORMS = ["sprites/Assets/platform.png"]
    ASSETS = [
        "sprites/Assets/Bush (1).png", "sprites/Assets/Bush (2).png", "sprites/Assets/Bush (3).png",
        "sprites/Assets/Bush (4).png", "sprites/Assets/Mushroom_1.png", "sprites/Assets/Mushroom_2.png",
        "sprites/Assets/Stone.png", "sprites/Assets/Tree_2.png", "sprites/Assets/Tree_3.png", "sprites/Assets/Sign_2.png"]
    BASE = ["sprites/Assets/base.png"]
    SAMPLE = ["sprites/sample.png"]

class EnemySprites:
    """
        Enemy sprites
    """
    ENEMY_IMAGE_LIST_LEFT = [
        "sprites/Enemy/Run_left (%i).png" % i for i in range(1, 10)]
    ENEMY_IMAGE_LIST_RIGHT = [
        "sprites/Enemy/Run_right (%i).png" % i for i in range(1, 10)]
