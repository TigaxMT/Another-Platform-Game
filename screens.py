import pygame
from settings import * # constants

class Screens:
    def __init__(self,game, screen,widgets): # Define important variables for the screens
        
        #Define class objects 
        self.screen = screen
        self.widgets = widgets
        self.game = game

        #Define the sample image for start and credits screens
        self.bg_img = pygame.image.load(SAMPLE[0])
        self.bg_img_rect = self.bg_img.get_rect()

        #Define variables for the color text in credits screen
        self.clr_prog = self.clr_sound = self.clr_design = BLACK

        #Define and initialize with random data the variable to manipulate and Draw Text Objects
        self.largeText = pygame.font.SysFont(None,80)
        self.TextSurf, TextRect = self.widgets.text_objects("Initialize with Random data", self.largeText,BLACK)

    def show_start_screen(self): # game splash/start screen

        # Kill all sprites if they exists
        if len(self.game.all_sprites) != 0:
            self.game.killAllSprites()

        pygame.mixer.music.stop()

        #Start Screen function main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.quit_game()

            #Fill screen with white color and draw the sample image initialized on __init__
            self.screen.fill(WHITE)
            self.screen.blit(self.bg_img,self.bg_img_rect)

            #Create a surface and rectangle for the Title text
            self.largeText = pygame.font.SysFont(None,80)
            self.TextSurf, self.TextRect = self.widgets.text_objects(TITLE, self.largeText,BLACK)
            self.TextRect.center = ((WIDTH/2),(HEIGHT- 500))
            self.screen.blit(self.TextSurf, self.TextRect)

            #Create start, credits and quit buttons
            self.widgets.button("Play!",150,450,100,50,GREEN,BRIGHT_GREEN,self.game.new)
            self.widgets.button("Credits",((150+550)/2),450,100,50,DARK_YELLOW,YELLOW,self.credits)
            self.widgets.button("Quit",550,450,100,50,RED,BRIGHT_RED,self.game.quit_game)

            pygame.display.flip()
            self.game.clock.tick(FPS)

    def game_over(self):
        #When player dies

        pygame.mixer.music.stop()
        self.screen.fill(WHITE)

        # Kill all sprites
        self.game.killAllSprites()
        
        #Create a surface and rectangle for the gameover text
        self.largeText = pygame.font.SysFont(None,115)
        self.TextSurf, self.TextRect = self.widgets.text_objects("You Died!", self.largeText,BLACK)
        self.TextRect.center = ((WIDTH/2),(HEIGHT/2))
        self.screen.blit(self.TextSurf, self.TextRect)

        #GameOver function main loop
        while True:
            for event in pygame.event.get():

                #Check if Quit event is called
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            #Create play and quit buttons
            self.widgets.button("Play Again",150,450,100,50,GREEN,BRIGHT_GREEN,self.game.new)
            self.widgets.button("Quit",550,450,100,50,RED,BRIGHT_RED,self.show_start_screen)

            pygame.display.flip()
            self.game.clock.tick(FPS)

    def paused(self): # When game pause

        pygame.mixer.music.pause()

        #Create a surface and rectangle for the Paused text
        self.largeText = pygame.font.SysFont(None,115)
        self.TextSurf, self.TextRect = self.widgets.text_objects("Paused", self.largeText,BLACK)
        self.TextRect.center = ((WIDTH/2),(HEIGHT/2))
        self.screen.blit(self.TextSurf, self.TextRect)

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
            self.widgets.button("Continue",150,450,100,50,GREEN,BRIGHT_GREEN,self.game.unpause)
            self.widgets.button("Quit",550,450,100,50,RED,BRIGHT_RED,self.show_start_screen)

            pygame.display.flip()
            self.game.clock.tick(FPS)

    def credits(self):
        
        #Randomize new colors
        self.clr_prog = pygame.Color(random.randrange(0,200),random.randrange(0,200),random.randrange(0,200))
        self.clr_sound = pygame.Color(random.randrange(0,200),random.randrange(0,200),random.randrange(0,200))
        self.clr_design = pygame.Color(random.randrange(0,200),random.randrange(0,200),random.randrange(0,200))

        #Credits function main loop
        while True:
            for event in pygame.event.get():
                #Check if Quit event is called
                if event.type == pygame.QUIT:
                    self.game.quit_game()
            
            #Variable to store the next height for the credits text
            height = 0

            #Draw the sample image
            self.screen.blit(self.bg_img,self.bg_img_rect)

            # Check the text credits columns
            for i in range(len(CREDITS)):
                #Draw each if statement text in a a different color
                if CREDITS[i] == "Programmers: Tiago Martins" or "Kelvin Ferreira":
                    self.largeText = pygame.font.SysFont(None,40)
                    self.TextSurf, self.TextRect = self.widgets.text_objects(CREDITS[i], self.largeText,self.clr_prog)

                if CREDITS[i] == "Sounds: Bruna Silva (Girlfriend of Tiago Martins)": 
                    self.largeText = pygame.font.SysFont(None,40)
                    self.TextSurf, self.TextRect = self.widgets.text_objects(CREDITS[i], self.largeText,self.clr_sound)

                if CREDITS[i] == "Designers: Zuhria Alfitra" or CREDITS[i] == "Tiago Martins":  
                    self.largeText = pygame.font.SysFont(None,40)
                    self.TextSurf, self.TextRect = self.widgets.text_objects(CREDITS[i], self.largeText,self.clr_design)

                #Increase the height variable
                height += 50

                #Some special positions for some credtis text, for all text stay align
                if CREDITS[i] == "Tiago Martins":
                    self.TextRect.x = 165
                    self.TextRect.y = height
                elif CREDITS[i] == "Kelvin Ferreira":
                    self.TextRect.x = 215
                    self.TextRect.y = height
                else:
                    self.TextRect.x = 10
                    self.TextRect.y = height
                
                #Draw the CREDITS[i] text
                self.screen.blit(self.TextSurf, self.TextRect)

            #Create a surface and rectangle for the Copyright text
            self.largeText = pygame.font.SysFont(None,30)
            self.TextSurf, self.TextRect = self.widgets.text_objects(" Copyright © 2017  Tiago Martins", self.largeText,BLACK)
            self.TextRect.center = ((WIDTH/2),(HEIGHT - 150))
            self.screen.blit(self.TextSurf, self.TextRect)

            #Create the Main Menu button
            self.widgets.button("Main Menu",((WIDTH - 150)/2),(HEIGHT - 90),100,50,BLUE,LIGHTBLUE,self.show_start_screen)
            
            #Reinitialize the height variable to return draw all text in the same y position
            height = 0
            
            pygame.display.flip()
            self.game.clock.tick(FPS)