"""
    A simple Game to test neural networks , machine learning etc

    Copyright (C) 2017  Tiago Martins, Kelvin Ferreira

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import random
import pygame

#Game controllers
from game_modules.controllers.asset import Asset
from game_modules.controllers.platform import Platform
from game_modules.controllers.base import Base
from game_modules.controllers.background import Background
from game_modules.controllers.enemy import Enemy

#settings imports
from game_modules.settings.sprites import EnemySprites
from game_modules.settings.sprites import PlatformSprites
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

        self.side_collide = False

        #Create all needed sprite groups
        self.platforms = pygame.sprite.Group()
        self.assets = pygame.sprite.Group()
        self.base = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
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
        
        if entity == "Enemy":
            while len(self.enemies) < 1:

                #Load the image: the Enemy class will load to get the height for spawn correctly the assets
                img = pygame.image.load(
                    EnemySprites.ENEMY_IMAGE_LIST_RIGHT[0]).convert_alpha()
                height_img = img.get_size()[1]

                e = Enemy(random.randrange(PlatformSettings.WIDTH, PlatformSettings.WIDTH + 250), 
                                            PlatformSettings.HEIGHT - (height_img + 71))
                
                self.enemies.add(e)
                self.all_sprites.add(e)

        elif entity == "Platform":

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

        if entity == "Enemy":
            #Moving each platform and kill platforms reach Width 0
            for enem in self.enemies:

                if self.game.player.vel.x > 0:
                    enem.rect.x -= abs(self.game.player.vel.x)
                if enem.rect.right < 0:
                    enem.kill()

        elif entity == "Platform":

            #Moving each platform and kill platforms reach Width 0
            for plat in self.platforms:

                if self.game.player.vel.x > 0 and self.side_collide == False:
                    plat.rect.x -= abs(self.game.player.vel.x)
                if plat.rect.right < 0:
                    plat.kill()

        elif entity == "Asset":

            #Moving each asset and kill assets reach Width 0
            for ass in self.assets:
                if self.game.player.vel.x > 0 and self.side_collide == False:
                    ass.rect.x -= abs(self.game.player.vel.x)
                if ass.rect.right < 0:
                    ass.kill()

        elif entity == "Base":

            #Moving each base and kill bases reach Width 0
            for bases in self.base:
                if self.game.player.vel.x > 0 and self.side_collide == False:
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
        self.enemies.empty()
