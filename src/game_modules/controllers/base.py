import pygame

from game_modules.settings.platform import PlatformSettings

class Base(pygame.sprite.Sprite):  # Creates a Base Sprite
    def __init__(self, image_file, x, y):

        #Initialize the Sprite function
        pygame.sprite.Sprite.__init__(self)

        #Create the surface to the image
        self.image = pygame.Surface((PlatformSettings.WIDTH, 71))

        #Load the image and get the rectangle of him
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()

        #Put the rectangle in the position
        self.rect.x = x
        self.rect.y = y