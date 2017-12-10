import pygame
import random

# Game screen and sprites
from game_modules.screen import Screen
from game_modules.sprites import Player, Asset, Platform, Base, Background

#settings imports
from game_modules.settings.sprites import PlayerSprites, PlatformSprites
from game_modules.settings.colors import GameColors
from game_modules.settings.platform import PlatformSettings

class LevelInfinite:
    def __init__(self,game):
        
        self.game = game

        self.small_text = None
        self.text_surf = None
        self.text_rect = None

        #Variable to store FPS
        self.fps = 0.0

        #Create all needed sprite groups
        self.platforms = pygame.sprite.Group()
        self.assets = pygame.sprite.Group()
        self.base = pygame.sprite.Group()
        self.background = None

        #Create and define already the main sprite group
        self.all_sprites = pygame.sprite.Group()


        #Define and initialize with random data the variable to manipulate and Draw Text Objects
        self.small_text = pygame.font.SysFont(None, 40)

        self.text_surf, self.text_rect = self.game.screen.widgets.text_objects(
            "FPS: " + str(self.fps), self.small_text, GameColors.BLACK)
    
    def initSprites(self):

        #Define the first platform_base position
        b = Base(PlatformSprites.BASE[0], 0, PlatformSettings.HEIGHT - 71)
        self.base.add(b)

        #Define the background image(sprite)
        self.background = Background(PlatformSprites.BACKGROUND[0], [0, 0])

        #Add to the main sprite group all the others sprite groups
        self.all_sprites.add(self.background)
        self.all_sprites.add(self.game.player)
        self.all_sprites.add(self.base)

    def randEntities(self,entity):
        
        if entity == "Platform":

            # Randomize platforms, only if don't have 1 spawned
            while len(self.platforms) < 1:
                p = Platform(random.randrange(PlatformSettings.WIDTH, PlatformSettings.WIDTH + 250),
                            random.randrange(
                                PlatformSettings.HEIGHT / 2,  PlatformSettings.HEIGHT - (71 + 71)),
                            195, 71)
                self.platforms.add(p)
                self.all_sprites.add(p)

        elif entity == "Asset":

            # Randomize assets, only if don't have 2 assets spawned
            while len(self.assets) < 2:
                n_img = random.randrange(0, len(PlatformSprites.ASSETS))

                #Load the image: the Asset class will load to get the height for spawn correctly the assets
                img = pygame.image.load(
                    PlatformSprites.ASSETS[n_img]).convert_alpha()
                height_img = img.get_size()[1]

                #Define a class Asset object and add it to the main sprite group
                a = Asset(PlatformSprites.ASSETS[n_img], random.randrange(
                    PlatformSettings.WIDTH, PlatformSettings.WIDTH + 250), PlatformSettings.HEIGHT - (height_img + 71))
                
                self.assets.add(a)
                self.all_sprites.add(a)

    def kill_move(self,entity):

        if entity == "Platform":

            #Moving each platform and kill platforms reach Width 0
            for plat in self.platforms:
                if self.game.player.vel.x > 0:
                    plat.rect.x -= abs(self.game.player.vel.x)
                if plat.rect.right < 0:
                    plat.kill()

        elif entity == "Asset":

            #Moving each asset and kill assets reach Width 0
            for ass in self.assets:
                if self.game.player.vel.x > 0:
                    ass.rect.x -= abs(self.game.player.vel.x)
                if ass.rect.right < 0:
                    ass.kill()

        elif entity == "Base":

            #Moving each base and kill bases reach Width 0
            for bases in self.base:
                if self.game.player.vel.x > 0:
                    bases.rect.x -= abs(self.game.player.vel.x)
                if bases.rect.right < 0:
                    bases.kill()

                #Randomize base platforms,only if don't have 2 bases spawned
                while len(self.base) < 2:
                    if bases.rect.right <= PlatformSettings.WIDTH:
                        base = Base(PlatformSprites.BASE[0], random.randrange(
                            PlatformSettings.WIDTH, PlatformSettings.WIDTH + 50),
                            PlatformSettings.HEIGHT - 71)
                        self.base.add(base)
                        self.all_sprites.add(base)

    def showFPS(self):  # Show FPS on screen

        #Update FPS variable
        self.fps = round(self.game.clock.get_fps())

        #Create and draw a surface and rectangle for the FPS text
        self.small_text = pygame.font.SysFont(None, 40)
        self.text_surf, self.text_rect = self.game.screen.widgets.text_objects(
            "FPS: " + str(self.fps), self.small_text, GameColors.BLACK)
        self.text_rect.x = 30
        self.text_rect.y = 30
        self.game.screen.surface.blit(self.text_surf, self.text_rect)
        
    def killAllSprites(self):  # Kill all Sprites

        self.all_sprites.empty()
        self.platforms.empty()
        self.assets.empty()
        self.base.empty()
