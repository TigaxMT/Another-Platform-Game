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

# Game screen and sprites
from game_modules.screen import Screen
from game_modules.sprites import Player, Asset, Platform, Base, Background

#settings imports
from game_modules.settings.sprites import PlayerSprites, PlatformSprites
from game_modules.settings.strings import GameTexts
from game_modules.settings.colors import GameColors
from game_modules.settings.audio import GameAudios
from game_modules.settings.platform import PlatformSettings

class Game:
    """
        Game is responsible for user interactions
    """

    def __init__(self):
        # Defining class variables
        self.player = None
        self.platforms = None
        self.small_text = None
        self.text_surf = None
        self.text_rect = None
        self.assets = None
        self.base = None
        self.background = None
        self.playing = None

        #Initialize pygame and mixer
        pygame.init()
        pygame.mixer.init()

        # Initializing
        self.screen = Screen(self)

        #Change the game icon and title
        img_icon = pygame.image.load(
            PlayerSprites.PLAYER_IMAGE_LIST_RIGHT[2]).convert_alpha()
        pygame.display.set_icon(img_icon)
        pygame.display.set_caption(GameTexts.TITLE)

        #Create and define already the main sprite group
        self.all_sprites = pygame.sprite.Group()

        #Define and initialize clock and boolean pause to know if game is paused or not
        self.clock = pygame.time.Clock()
        self.pause = False

        #Variable to store FPS
        self.fps = 0.0

        #Define and initialize with random data the variable to manipulate and Draw Text Objects
        self.small_text = pygame.font.SysFont(None, 40)

        self.text_surf, self.text_rect = self.screen.widgets.text_objects(
            "FPS: " + str(self.fps), self.small_text, GameColors.BLACK)

    def show_menu(self):
        """
            Show the main menu
        """
        self.screen.show_start_screen()

    def new(self):  # Start a new game

        # Kill all sprites if they exists
        if len(self.all_sprites) != 0:
            self.killAllSprites()

        #Loading and playing the main soundtrack
        pygame.mixer.music.load(GameAudios.MUSIC[0])
        pygame.mixer.music.play(-1)

        #Define a object to Player Class (sprite player class)
        self.player = Player(self)

        #Create all needed sprite groups
        self.platforms = pygame.sprite.Group()
        self.assets = pygame.sprite.Group()
        self.base = pygame.sprite.Group()

        #Define the first platform_base position
        b = Base(PlatformSprites.BASE[0], 0, PlatformSettings.HEIGHT - 71)
        self.base.add(b)

        #Define the background image(sprite)
        self.background = Background(PlatformSprites.BACKGROUND[0], [0, 0])

        #Add to the main sprite group all the others sprite groups
        self.all_sprites.add(self.background)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.base)

        #Call the main loop function
        self.run()

    def run(self):  # Game Loop

        self.playing = True

        # Main Loop
        while self.playing:
            self.clock.tick(PlatformSettings.FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):  # Game Loop - Update

        self.all_sprites.update()

        #Get all keys pressed
        keys = pygame.key.get_pressed()

        # check if player collide a platform when it's falling
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(
                self.player, self.platforms, False)
            hits_base = pygame.sprite.spritecollide(
                self.player, self.base, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

            elif hits_base:
                self.player.pos.y = hits_base[0].rect.top
                self.player.vel.y = 0

        # check if player collide a platform when jump
        elif self.player.vel.y < 0:
            for plat in self.platforms:
                if self.player.rect.colliderect(plat.rect):
                    if self.player.vel.y < 0:  # Moving up; Hit the bottom side of the wall
                        self.player.rect.top = plat.rect.bottom
                        self.player.vel.y = 10

        # if player reaches 0 width, platforms and assets stop moving

        if self.player.pos.x <= 0:
            self.player.pos.x = 0

        # if player reaches WIDTH - 250 , player stay running in the same position (WIDTH - 250)
        if self.player.rect.right >= (PlatformSettings.WIDTH - 250):
            self.player.pos.x -= abs(self.player.vel.x)

            # Only if the player moves to right, platforms and assets move
            if keys[pygame.K_RIGHT]:

                #Moving each platform and kill platforms reach Width 0
                for plat in self.platforms:
                    if self.player.vel.x > 0:
                        plat.rect.x -= abs(self.player.vel.x)
                    if plat.rect.right < 0:
                        plat.kill()

                #Moving each asset and kill assets reach Width 0
                for ass in self.assets:
                    if self.player.vel.x > 0:
                        ass.rect.x -= abs(self.player.vel.x)
                    if ass.rect.right < 0:
                        ass.kill()

                #Moving each base and kill bases reach Width 0
                for bases in self.base:
                    if self.player.vel.x > 0:
                        bases.rect.x -= abs(self.player.vel.x)
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

        # Randomize platforms, only if don't have 1 spawned
        while len(self.platforms) < 1:
            p = Platform(random.randrange(PlatformSettings.WIDTH, PlatformSettings.WIDTH + 250),
                         random.randrange(
                             PlatformSettings.HEIGHT / 2,  PlatformSettings.HEIGHT - (71 + 71)),
                         195, 71)
            self.platforms.add(p)
            self.all_sprites.add(p)

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

        # If player fall down
        if self.player.rect.bottom >= PlatformSettings.HEIGHT:
            self.screen.game_over()

    def events(self):  # Game Loop - events

        for event in pygame.event.get():

            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False

            # check if any key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    self.player.jump()
                if event.key == pygame.K_ESCAPE:
                    if self.pause == True:
                        self.unpause()
                    elif self.pause == False:
                        self.pause = True
                        self.screen.paused()

    def draw(self):  # Game Loop - draw

        self.screen.surface.fill(GameColors.WHITE)
        self.all_sprites.draw(self.screen.surface)

        #Draw FPS
        self.showFPS()

        # after drawing everything, flip(update) the display
        pygame.display.flip()

    def showFPS(self):  # Show FPS on screen

        #Update FPS variable
        self.fps = round(self.clock.get_fps())

        #Create and draw a surface and rectangle for the FPS text
        self.small_text = pygame.font.SysFont(None, 40)
        self.text_surf, self.text_rect = self.screen.widgets.text_objects(
            "FPS: " + str(self.fps), self.small_text, GameColors.BLACK)
        self.text_rect.x = 30
        self.text_rect.y = 30
        self.screen.surface.blit(self.text_surf, self.text_rect)

    def killAllSprites(self):  # Kill all Sprites

        self.all_sprites.empty()
        self.platforms.empty()
        self.assets.empty()
        self.base.empty()

    def unpause(self):  # Unpause the game

        self.pause = False
        pygame.mixer.music.unpause()

    def quit_game(self):  # Close the Game

        pygame.quit()
        quit()


# Create an Object of the Game Class
g = Game()

#Call the start screen funcion
g.show_menu()
