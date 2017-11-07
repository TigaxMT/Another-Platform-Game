# game options/settings
import random

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

#Images for Sprite Animation
PLAYER_IMAGE_LIST_LEFT = ["sprites/left_0.png","sprites/left_1.png","sprites/left_2.png"]
PLAYER_IMAGE_LIST_RIGHT = ["sprites/right_0.png","sprites/right_1.png","sprites/right_2.png"]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BRIGHT_RED = (255,0,0)
BRIGHT_GREEN = (0,255,0)
