import pygame
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window, mixer, clock
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.pause = False

    def new(self):
        # start a new game
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        # Randomize platforms
        rand_platforms()
        for plat in PLATFORM_LIST:
            p = Platform(plat[0],plat[1],plat[2],plat[3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platform when it's falling
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                if event.key == pygame.K_ESCAPE:
                    self.pause = True
                    self.paused()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(LIGHTBLUE)
        self.all_sprites.draw(self.screen)
        # after drawing everything, flip the display
        pygame.display.flip()

    def text_objects(self,text, font):
        # Creates Text Messages
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()

    def button(self,msg,x,y,w,h,ic,ac,action=None):
        # Create Buttons
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print(click)
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.screen, ac,(x,y,w,h))
            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(self.screen, ic,(x,y,w,h))
            smallText = pygame.font.SysFont("comicsansms",20)
            textSurf, textRect = self.text_objects(msg, smallText)
            textRect.center = ( (x+(w/2)), (y+(h/2)) )
            self.screen.blit(textSurf, textRect)

    def quit_game(self):
        # Close the Game
        pygame.quit()
        quit()

    def show_start_screen(self):
        # game splash/start screen
        start_screen = True

        while start_screen:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    self.running = False
                    self.quit_game()

            self.screen.fill(WHITE)
            largeText = pygame.font.SysFont("comicsansms",80)
            TextSurf, TextRect = self.text_objects(TITLE, largeText)
            TextRect.center = ((WIDTH/2),(HEIGHT/2))
            self.screen.blit(TextSurf, TextRect)

            self.button("Play!",150,450,100,50,GREEN,BRIGHT_GREEN,self.new)
            self.button("Quit",550,450,100,50,RED,BRIGHT_RED,self.quit_game)

            pygame.display.update()
            self.clock.tick(15)
    def unpause(self):
        # Unpause the game
        self.pause = False
        pygame.mixer.music.unpause()

    def paused(self):
        # When game pause
        pygame.mixer.music.pause()
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = self.text_objects("Paused", largeText)
        TextRect.center = ((WIDTH/2),(HEIGHT/2))
        self.screen.blit(TextSurf, TextRect)


        while self.pause:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()

            self.button("Continue",150,450,100,50,GREEN,BRIGHT_GREEN,self.unpause)
            self.button("Quit",550,450,100,50,RED,BRIGHT_RED,self.show_start_screen)

            pygame.display.update()
            self.clock.tick(15)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()
quit()
