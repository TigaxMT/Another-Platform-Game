
import pygame


class Background(pygame.sprite.Sprite):  # Creates a Background Sprite
    def __init__(self, image_file, location):

        #Initialize the Sprite function
        pygame.sprite.Sprite.__init__(self)

        #Load the image file and get the rectangle of him
        self.image = pygame.image.load(image_file).convert_alpha()

        #Put the rectangle in the position
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
