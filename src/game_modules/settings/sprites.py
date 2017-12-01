"""
    Constants for sprite animation
"""

class PlayerSprites:
    """
        Player sprites
    """
    PLAYER_IMAGE_LIST_LEFT = [
        "sprites/Run_left (%i).png" % i for i in range(1, 9)]
    PLAYER_IMAGE_LIST_RIGHT = [
        "sprites/Run_right (%i).png" % i for i in range(1, 9)]
    PLAYER_IMAGE_STOPPED = ["sprites/Idle (%i).png" % i for i in range(1, 11)]


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
