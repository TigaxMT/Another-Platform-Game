
import pygame

class Asset(pygame.sprite.Sprite):  # Creates a Asset Sprite
    def __init__(self, image_file, x, y):

        #Initialize the Sprite function
        pygame.sprite.Sprite.__init__(self)

        #Load the image file and get the rectangle of him
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()

        #Put the rectangle in the position
        self.rect.x = x
        self.rect.y = y