import pygame
import random

from game_modules.settings.player import PlayerSettings
from game_modules.settings.sprites import EnemySprites
from game_modules.settings.platform import PlatformSettings
from game_modules.settings.audio import GameAudios

vec = pygame.math.Vector2  # define a variable vectors for the movements

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

        #Define the vectors of position , velocity and acceleration
        self.pos = vec(random.randrange(PlatformSettings.WIDTH,PlatformSettings.WIDTH + 250),
                       PlatformSettings.HEIGHT - 71)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        #Define the stop enemy sprite and get the rectangle of him
        self.image = pygame.image.load(
            EnemySprites.ENEMY_IMAGE_STOPPED[0]).convert_alpha()
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

            #Put an positive(oposite for the left movement) constant acceleration to the enemy to give better physics
            self.acc.x = PlayerSettings.PLAYER_ACC
            self.counter_right += 1

            self.steps_right += 1

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

            #Put an negative(oposite for the right movement) constant acceleration to the player to give better physics
            self.acc.x = -PlayerSettings.PLAYER_ACC
            self.counter_left += 1

            self.steps_left += 1


        # apply friction to the acceleration
        self.acc.x += self.vel.x * PlayerSettings.PLAYER_FRICTION

        # equations of motion
        self.vel += self.acc
        #self.pos += self.vel + 0.5 * self.acc
        #self.rect.midbottom = self.pos

        # Animation of the Enemy Idle Sprite 
        if self.counter_stopped == 8:
            self.counter_stopped = 0
        
        elif self.counter_stopped < 8:
            self.counter_stopped += 1

        self.image = pygame.image.load(
                EnemySprites.ENEMY_IMAGE_STOPPED[self.counter_stopped]).convert_alpha()
