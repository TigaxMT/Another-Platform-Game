import pygame
from settings import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        # Pass a game instance of our Game Class for player to has access of the Game vars/funcs etc
        self.game = game
        self.image = pygame.image.load("sprites/right_1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        # Use 2 counter vars to know what image use
        self.counter_right = 0
        self.counter_left = 0
        # direc var is use for set the player direction when it is stopped
        self.direc = "right"

    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20

    def update(self):
        # Update Sprites on the screen
        self.acc = vec(0, PLAYER_GRAV)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            # Verify if is the last image of the sprite animation, if it was restart the counter
            if self.counter_left == 2:
                self.counter_left = 0
            self.image = pygame.image.load(PLAYER_IMAGE_LIST_LEFT[self.counter_left])
            self.acc.x = -PLAYER_ACC
            self.counter_left += 1
            self.direc = 'left'

        if keys[pygame.K_RIGHT]:
            # Verify if is the last image of the sprite animation, if it was restart the counter
            if self.counter_right == 2:
                self.counter_right = 0
            self.image = pygame.image.load(PLAYER_IMAGE_LIST_RIGHT[self.counter_right])
            self.acc.x = PLAYER_ACC
            self.counter_right += 1
            self.direc = 'right'

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

        # Set the Player Sprite Animation Stopped
        if self.vel.x == 0:
            if self.direc == 'left':
                self.image = pygame.image.load("sprites/left_1.png")
            elif self.direc == 'right':
                self.image = pygame.image.load("sprites/right_1.png")


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
