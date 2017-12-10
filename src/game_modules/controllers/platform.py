
import pygame

from game_modules.settings.sprites import PlatformSprites

class Platform(pygame.sprite.Sprite):  # Creates a Platform Sprite
    def __init__(self, x, y, w, h):

        #Initialize the Sprite function
        pygame.sprite.Sprite.__init__(self)

        #Create the surface to the image
        self.image = pygame.Surface((w, h))

        #Load the image and get the rectangle of him
        self.image = pygame.image.load(
            PlatformSprites.PLATFORMS[0]).convert_alpha()
        self.rect = self.image.get_rect()

        #Put the rectangle in the position
        self.rect.x = x
        self.rect.y = y