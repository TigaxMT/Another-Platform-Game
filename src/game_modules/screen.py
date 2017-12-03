"""
    Screen module
"""

import random
import pygame

from game_modules.widgets import Widgets

#settings
from game_modules.settings.colors import GameColors
from game_modules.settings.platform import PlatformSettings
from game_modules.settings.sprites import PlatformSprites
from game_modules.settings.strings import GameTexts
from game_modules.settings.credits import GameCredits


class Screen:
    """
        Scren is responsible to render data on screen
    """

    def __init__(self, game):  # Define important variables for the screens
        # Define class objects
        self.surface = pygame.display.set_mode(
            (PlatformSettings.WIDTH, PlatformSettings.HEIGHT))  # Creating the surface
        self.widgets = Widgets(self.surface)
        self.game = game

        #Define the sample image for start and credits screens
        self.bg_img = pygame.image.load(PlatformSprites.SAMPLE[0])
        self.bg_img_rect = self.bg_img.get_rect()

        #Define variables for the color text in credits screen
        self.clr_prog = self.clr_sound = self.clr_design = GameColors.BLACK

        #Define and initialize with random data the variable to manipulate and Draw Text Objects
        self.largeText = pygame.font.SysFont(None, 80)
        self.TextSurf, TextRect = self.widgets.text_objects(
            "Initialize with Random data", self.largeText, GameColors.BLACK)

    def show_start_screen(self):  # game splash/start screen

        # Kill all sprites if they exists
        if len(self.game.level.all_sprites) != 0:
            self.game.level.killAllSprites()

        pygame.mixer.music.stop()

        #Start Screen function main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.quit_game()

            #Fill screen with white color and draw the sample image initialized on __init__
            self.surface.fill(GameColors.WHITE)
            self.surface.blit(self.bg_img, self.bg_img_rect)

            #Create a surface and rectangle for the Title text
            self.largeText = pygame.font.SysFont(None, 80)
            self.TextSurf, self.TextRect = self.widgets.text_objects(
                GameTexts.TITLE, self.largeText, GameColors.BLACK)
            self.TextRect.center = (
                (PlatformSettings.WIDTH / 2), (PlatformSettings.HEIGHT - 500))
            self.surface.blit(self.TextSurf, self.TextRect)

            #Create start, credits and quit buttons
            self.widgets.button("Play!", 150, 450, 100, 50,
                                GameColors.GREEN, GameColors.BRIGHT_GREEN, self.game.new)
            self.widgets.button("Credits", ((150 + 550) / 2),
                                450, 100, 50, GameColors.DARK_YELLOW, GameColors.YELLOW, self.credits)
            self.widgets.button("Quit", 550, 450, 100, 50,
                                GameColors.RED, GameColors.BRIGHT_RED, self.game.quit_game)

            pygame.display.flip()
            self.game.clock.tick(PlatformSettings.FPS)

    def game_over(self):
        #When player dies

        pygame.mixer.music.stop()
        self.surface.fill(GameColors.WHITE)

        # Kill all sprites
        self.game.level.killAllSprites()

        #Create a surface and rectangle for the gameover text
        self.largeText = pygame.font.SysFont(None, 115)
        self.TextSurf, self.TextRect = self.widgets.text_objects(
            "You Died!", self.largeText, GameColors.BLACK)
        self.TextRect.center = (
            (PlatformSettings.WIDTH / 2), (PlatformSettings.HEIGHT / 2))
        self.surface.blit(self.TextSurf, self.TextRect)

        #GameOver function main loop
        while True:
            for event in pygame.event.get():

                #Check if Quit event is called
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            #Create play and quit buttons
            self.widgets.button("Play Again", 150, 450, 100,
                                50, GameColors.GREEN, GameColors.BRIGHT_GREEN, self.game.new)
            self.widgets.button("Quit", 550, 450, 100, 50,
                                GameColors.RED, GameColors.BRIGHT_RED, self.show_start_screen)

            pygame.display.flip()
            self.game.clock.tick(PlatformSettings.FPS)

    def paused(self):  # When game pause

        pygame.mixer.music.pause()

        #Create a surface and rectangle for the Paused text
        self.largeText = pygame.font.SysFont(None, 115)
        self.TextSurf, self.TextRect = self.widgets.text_objects(
            "Paused", self.largeText, GameColors.BLACK)
        self.TextRect.center = (
            (PlatformSettings.WIDTH / 2), (PlatformSettings.HEIGHT / 2))
        self.surface.blit(self.TextSurf, self.TextRect)

        #Paused function main loop
        while self.game.pause:
            for event in pygame.event.get():

                #Check if Quit event is called
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()

                #Check if any key is pressed
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        if self.game.pause == True:
                            self.game.unpause()

            #Create cotninue and quit buttons
            self.widgets.button("Continue", 150, 450, 100,
                                50, GameColors.GREEN, GameColors.BRIGHT_GREEN, self.game.unpause)
            self.widgets.button("Quit", 550, 450, 100, 50,
                                GameColors.RED, GameColors.BRIGHT_RED, self.show_start_screen)

            pygame.display.flip()
            self.game.clock.tick(PlatformSettings.FPS)

    def credits(self):

        #Randomize new colors
        self.clr_prog = pygame.Color(random.randrange(
            0, 200), random.randrange(0, 200), random.randrange(0, 200))
        self.clr_sound = pygame.Color(random.randrange(
            0, 200), random.randrange(0, 200), random.randrange(0, 200))
        self.clr_design = pygame.Color(random.randrange(
            0, 200), random.randrange(0, 200), random.randrange(0, 200))

        #Credits function main loop
        while True:
            for event in pygame.event.get():
                #Check if Quit event is called
                if event.type == pygame.QUIT:
                    self.game.quit_game()

            #Variable to store the next height for the credits text
            height = 0

            #Draw the sample image
            self.surface.blit(self.bg_img, self.bg_img_rect)

            # Check the text credits columns
            for i in range(len(GameCredits.CREDITS)):
                #Draw each if statement text in a a different color
                if GameCredits.CREDITS[i] == "Programmers: Tiago Martins" or "Kelvin Ferreira":
                    self.largeText = pygame.font.SysFont(None, 40)
                    self.TextSurf, self.TextRect = self.widgets.text_objects(
                        GameCredits.CREDITS[i], self.largeText, self.clr_prog)

                if GameCredits.CREDITS[i] == "Sounds: Bruna Silva (Girlfriend of Tiago Martins)":
                    self.largeText = pygame.font.SysFont(None, 40)
                    self.TextSurf, self.TextRect = self.widgets.text_objects(
                        GameCredits.CREDITS[i], self.largeText, self.clr_sound)

                if GameCredits.CREDITS[i] == "Designers: Zuhria Alfitra":
                    self.largeText = pygame.font.SysFont(None, 40)
                    self.TextSurf, self.TextRect = self.widgets.text_objects(
                        GameCredits.CREDITS[i], self.largeText, self.clr_design)

                #Increase the height variable
                height += 50

                #Some special positions for some credtis text, for all text stay align
                if GameCredits.CREDITS[i] == "Kelvin Ferreira":
                    self.TextRect.x = 215
                    self.TextRect.y = height
                else:
                    self.TextRect.x = 10
                    self.TextRect.y = height

                #Draw the GameCredits.CREDITS[i] text
                self.surface.blit(self.TextSurf, self.TextRect)

            #Create a surface and rectangle for the Copyright text
            self.largeText = pygame.font.SysFont(None, 30)
            self.TextSurf, self.TextRect = self.widgets.text_objects(
                " Copyright © 2017  Tiago Martins", self.largeText, GameColors.BLACK)
            self.TextRect.center = (
                (PlatformSettings.WIDTH / 2), (PlatformSettings.HEIGHT - 150))
            self.surface.blit(self.TextSurf, self.TextRect)

            #Create the Main Menu button
            self.widgets.button("Main Menu", ((PlatformSettings.WIDTH - 150) / 2), (PlatformSettings.HEIGHT - 90),
                                100, 50, GameColors.BLUE, GameColors.LIGHTBLUE, self.show_start_screen)

            #Reinitialize the height variable to return draw all text in the same y position
            height = 0

            pygame.display.flip()
            self.game.clock.tick(PlatformSettings.FPS)
