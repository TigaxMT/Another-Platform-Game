import pygame
import random

from game_modules.settings.player import PlayerSettings
from game_modules.settings.sprites import EnemySprites
from game_modules.settings.platform import PlatformSettings
from game_modules.settings.audio import GameAudios

class Enemy(pygame.sprite.Sprite): # Creates a Enemy Sprite
    def __init__(self,x,y):
        
        #Initialize the Sprite function
        pygame.sprite.Sprite.__init__(self)

        # Use 3 counter variables to know what image use
        self.counter_right = 0
        self.counter_left = 0
        self.counter_stopped = 0

        # Count the steps 
        self.steps_right = 0
        self.steps_left = 0

        #Define the stop enemy sprite and get the rectangle of him
        self.image = pygame.image.load(
            EnemySprites.ENEMY_IMAGE_LIST_RIGHT[0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        
        if self.steps_right < 100:

            # Reset right steps
            if self.steps_left != 0 and self.steps_right == 98:
                self.steps_left = 0

            # Verify if is the last image of the sprite animation, if it was restart the counter
            if self.counter_right == 8:
                self.counter_right = 0

            #Update the enemy image with the correct image, to give the sensation of movement
            self.image = pygame.image.load(
                EnemySprites.ENEMY_IMAGE_LIST_RIGHT[self.counter_right]).convert_alpha()

            self.counter_right += 1

            self.steps_right += 1

            self.rect.x += 5

        elif self.steps_left < 100:

            # Reset right steps
            if self.steps_right != 0 and self.steps_left == 98:
                self.steps_right = 0
            
            # Verify if is the last image of the sprite animation, if it was restart the counter
            if self.counter_left == 8:
                self.counter_left = 0

            #Update the player image with the correct image, to give the sensation of movement
            self.image = pygame.image.load(
                EnemySprites.ENEMY_IMAGE_LIST_LEFT[self.counter_left]).convert_alpha()

            self.counter_left += 1

            self.steps_left += 1

            self.rect.x -= 5

                