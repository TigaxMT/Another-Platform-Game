import pygame
from settings import *

class Screens:
    def __init__(self,game, screen,widgets):
        self.screen = screen
        self.widgets = widgets
        self.game = game
    
    def show_start_screen(self):
        # game splash/start screen

        pygame.mixer.music.stop()
        bg_img = pygame.image.load(SAMPLE[0])
        bg_img_rect = bg_img.get_rect()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.quit_game()

            self.screen.fill(WHITE)
            self.screen.blit(bg_img,bg_img_rect)
            largeText = pygame.font.SysFont(None,80)
            TextSurf, TextRect = self.widgets.text_objects(TITLE, largeText,BLACK)
            TextRect.center = ((WIDTH/2),(HEIGHT- 500))
            self.screen.blit(TextSurf, TextRect)

            self.widgets.button("Play!",150,450,100,50,GREEN,BRIGHT_GREEN,self.game.new)
            self.widgets.button("Credits",((150+550)/2),500,100,50,DARK_YELLOW,YELLOW,self.credits)
            self.widgets.button("Quit",550,450,100,50,RED,BRIGHT_RED,self.game.quit_game)

            pygame.display.flip()
            self.game.clock.tick(FPS)

    def game_over(self):
        #When player dies

        pygame.mixer.music.stop()

        self.screen.fill(WHITE)

        largeText = pygame.font.SysFont(None,115)
        TextSurf, TextRect = self.widgets.text_objects("You Died!", largeText,BLACK)
        TextRect.center = ((WIDTH/2),(HEIGHT/2))
        self.screen.blit(TextSurf, TextRect)

        while True:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.widgets.button("Play Again",150,450,100,50,GREEN,BRIGHT_GREEN,self.game.new)
            self.widgets.button("Quit",550,450,100,50,RED,BRIGHT_RED,self.show_start_screen)

            pygame.display.flip()
            self.game.clock.tick(15)

    def paused(self):
        # When game pause
        pygame.mixer.music.pause()
        largeText = pygame.font.SysFont(None,115)
        TextSurf, TextRect = self.widgets.text_objects("Paused", largeText,BLACK)
        TextRect.center = ((WIDTH/2),(HEIGHT/2))
        self.screen.blit(TextSurf, TextRect)


        while self.game.pause:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.game.pause == True:
                            self.game.unpause()

            self.widgets.button("Continue",150,450,100,50,GREEN,BRIGHT_GREEN,self.game.unpause)
            self.widgets.button("Quit",550,450,100,50,RED,BRIGHT_RED,self.show_start_screen)

            pygame.display.flip()
            self.game.clock.tick(FPS)

    def credits(self):
        clr_prog = clr_sound = clr_design = BLACK
        bg_img = pygame.image.load(SAMPLE[0])
        bg_img_rect = bg_img.get_rect()

        clr_prog = (random.randrange(0,200),random.randrange(0,200),random.randrange(0,200))
        clr_sound = (random.randrange(0,200),random.randrange(0,200),random.randrange(0,200))
        clr_design = (random.randrange(0,200),random.randrange(0,200),random.randrange(0,200))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running = False
                    self.game.quit_game()

            # Show credits
            height = 0
            self.screen.blit(bg_img,bg_img_rect)

            for i in range(len(CREDITS)):

                if CREDITS[i] == "Programmers: Tiago Martins" or "Kelvin Ferreira":
                    largeText = pygame.font.SysFont(None,40)
                    TextSurf, TextRect = self.widgets.text_objects(CREDITS[i], largeText,clr_prog)
                if CREDITS[i] == "Sounds: Bruna Silva (Girlfriend of Tiago Martins)": 
                    largeText = pygame.font.SysFont(None,40)
                    TextSurf, TextRect = self.widgets.text_objects(CREDITS[i], largeText,clr_sound)
                if CREDITS[i] == "Designers: Zuhria Alfitra" or CREDITS[i] == "Tiago Martins":  
                    largeText = pygame.font.SysFont(None,40)
                    TextSurf, TextRect = self.widgets.text_objects(CREDITS[i], largeText,clr_design)

                height += 50
                if CREDITS[i] == "Tiago Martins":
                    TextRect.x = 165
                    TextRect.y = height
                elif CREDITS[i] == "Kelvin Ferreira":
                    TextRect.x = 215
                    TextRect.y = height
                else:
                    TextRect.x = 10
                    TextRect.y = height
                self.screen.blit(TextSurf, TextRect)


            largeText = pygame.font.SysFont(None,30)
            TextSurf, TextRect = self.widgets.text_objects(" Copyright © 2017  Tiago Martins", largeText,BLACK)
            TextRect.center = ((WIDTH/2),(HEIGHT - 150))
            self.screen.blit(TextSurf, TextRect)

            self.widgets.button("Main Menu",((WIDTH - 150)/2),(HEIGHT - 100),100,50,BLUE,LIGHTBLUE,self.show_start_screen)
            height = 0
            
            pygame.display.flip()