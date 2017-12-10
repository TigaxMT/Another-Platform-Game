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

import pygame

#Game screen & levels
from game_modules.screen import Screen
from game_modules.levels.level_infinite import LevelInfinite

#Game controllers
from game_modules.controllers.player import Player
from game_modules.controllers.asset import Asset
from game_modules.controllers.platform import Platform
from game_modules.controllers.base import Base
from game_modules.controllers.background import Background

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
        self.playing = None

        #Initialize pygame and mixer
        pygame.init()
        pygame.mixer.init()

        # Initializing
        self.screen = Screen(self)
        self.player = Player(self)
        self.level = LevelInfinite(self)

        #Change the game icon and title
        img_icon = pygame.image.load(
            PlayerSprites.PLAYER_IMAGE_LIST_RIGHT[2]).convert_alpha()
        pygame.display.set_icon(img_icon)
        pygame.display.set_caption(GameTexts.TITLE)

        #Define and initialize clock and boolean pause to know if game is paused or not
        self.clock = pygame.time.Clock()
        self.pause = False

    def show_menu(self):
        """
            Show the main menu
        """
        self.screen.show_start_screen()

    def new(self):  # Start a new game

        # Kill all sprites if they exists
        if len(self.level.all_sprites) != 0:
            self.level.killAllSprites()

        #Stop the menu music
        pygame.mixer.music.stop()

        #Loading and playing the main soundtrack
        pygame.mixer.music.load(GameAudios.MUSIC[0])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        #Call the main loop function
        self.run()

    def run(self):  # Game Loop

        self.playing = True

        self.level.initSprites()

        # Main Loop
        while self.playing:
            self.clock.tick(PlatformSettings.FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):  # Game Loop - Update

        self.level.all_sprites.update()

        #Get all keys pressed
        keys = pygame.key.get_pressed()

        #Verify if player collide with any platform
        self.player.collisionDetection()

        # if player reaches 0 width, platforms and assets stop moving

        if self.player.pos.x <= 0:
            self.player.pos.x = 0

        # if player reaches WIDTH - 250 , player stay running in the same position (WIDTH - 250)
        if self.player.rect.right >= (PlatformSettings.WIDTH - 250):
            self.player.pos.x -= abs(self.player.vel.x)

        # Only if the player moves to right, platforms and assets move
        if keys[pygame.K_RIGHT]:

            #Verify if is need to kill or move a platform
            self.level.kill_move("Platform")

            #Verify if is need to kill or move a asset
            self.level.kill_move("Asset")

            #Verify if is need to kill or move a base
            self.level.kill_move("Base")

        # Verify if is need to randomize any entity
        if len(self.level.platforms) < 1:
            self.level.randEntities("Platform")

        if len(self.level.assets) < 2:
            self.level.randEntities("Asset")

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

        self.level.all_sprites.draw(self.screen.surface)

        #Draw FPS
        self.level.showFPS()

        # after drawing everything, flip(update) the display
        pygame.display.flip()

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
