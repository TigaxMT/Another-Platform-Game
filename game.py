"""
    A simple Game to test neural networks , machine learning etc

    Copyright (C) 2017  Tiago Martins

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
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # Initialize game window, mixer, clock etc
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.pause = False

    def new(self):
        # Start a new game
        pygame.mixer.music.load(MUSIC[0])
        pygame.mixer.music.play(-1)
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.background = Background(BG[0], [0,0])
        self.base = pygame.sprite.Group()
        b = Base(BASE[0],0 , HEIGHT-71)
        self.base.add(b)
        self.player = Player(self)
        self.all_sprites.add(self.background)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.base)
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
            hits_base = pygame.sprite.spritecollide(self.player, self.base, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

            elif hits_base:
                self.player.pos.y = hits_base[0].rect.top
                self.player.vel.y = 0

        # if player reaches WIDTH - 250

        keys = pygame.key.get_pressed()

        if self.player.pos.x <= 0:
            self.player.pos.x = 0

        if self.player.rect.right >= (WIDTH - 250):
            self.player.pos.x -= abs(self.player.vel.x)

            # Only if the player moves to right platforms move
            if keys[pygame.K_RIGHT]:
                for plat in self.platforms:
                    if self.player.vel.x > 0:
                        plat.rect.x -= abs(self.player.vel.x )
                    if plat.rect.right < 0:
                        plat.kill()

                # Give the base platform movement for each platform
                for bases in self.base:
                    if self.player.vel.x > 0:
                        bases.rect.x -= abs(self.player.vel.x )
                    if bases.rect.right < 0:
                        bases.kill()
                    #Randomize base platforms
                    while len(self.base) < 2:
                        if bases.rect.right <= WIDTH:
                            b = Base(BASE[0], WIDTH , HEIGHT - 71)
                            self.base.add(b)
                            self.all_sprites.add(b)

        # Randomize platforms
        while len(self.platforms) < 1:
            p = Platform(random.randrange(0, WIDTH),
                            random.randrange(HEIGHT / 2,  HEIGHT - (71+71)),
                            195, 71)
            self.platforms.add(p)
            self.all_sprites.add(p)

        # If player fall down
        if self.player.rect.bottom >= HEIGHT:
            self.game_over()

    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    self.player.jump()
                if event.key == pygame.K_ESCAPE:
                    if self.pause == True:
                        self.unpause()
                    elif self.pause == False:
                        self.pause = True
                        self.paused()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        # after drawing everything, flip the display
        pygame.display.flip()

    # ---------------- Screens Functions ----------------

    def show_start_screen(self):
        # game splash/start screen

        pygame.mixer.music.stop()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.quit_game()

            self.screen.fill(WHITE)
            largeText = pygame.font.SysFont(None,80)
            TextSurf, TextRect = self.text_objects(TITLE, largeText)
            TextRect.center = ((WIDTH/2),(HEIGHT/2))
            self.screen.blit(TextSurf, TextRect)

            self.button("Play!",150,450,100,50,GREEN,BRIGHT_GREEN,self.new)
            self.button("Credits",((150+550)/2),500,100,50,DARK_YELLOW,YELLOW,self.credits)
            self.button("Quit",550,450,100,50,RED,BRIGHT_RED,self.quit_game)

            pygame.display.flip()
            self.clock.tick(15)

    def game_over(self):
        #When player dies

        pygame.mixer.music.stop()

        self.screen.fill(WHITE)

        largeText = pygame.font.SysFont(None,115)
        TextSurf, TextRect = self.text_objects("You Died!", largeText)
        TextRect.center = ((WIDTH/2),(HEIGHT/2))
        self.screen.blit(TextSurf, TextRect)

        while True:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.button("Play Again",150,450,100,50,GREEN,BRIGHT_GREEN,self.new)
            self.button("Quit",550,450,100,50,RED,BRIGHT_RED,self.show_start_screen)

            pygame.display.flip()
            self.clock.tick(15)

    def paused(self):
        # When game pause
        pygame.mixer.music.pause()
        largeText = pygame.font.SysFont(None,115)
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.pause == True:
                            self.unpause()

            self.button("Continue",150,450,100,50,GREEN,BRIGHT_GREEN,self.unpause)
            self.button("Quit",550,450,100,50,RED,BRIGHT_RED,self.show_start_screen)

            pygame.display.flip()
            self.clock.tick(15)

    def credits(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.quit_game()

            height = 0
            width = 0
            self.screen.fill(WHITE)
            for i in range(len(CREDITS)):
                largeText = pygame.font.SysFont(None,40)
                TextSurf, TextRect = self.text_objects(CREDITS[i], largeText)
                height += 100
                TextRect.center = ((350),(height))
                self.screen.blit(TextSurf, TextRect)

            self.button("Main Menu",((WIDTH - 150)/2),(HEIGHT - 100),100,50,BLUE,LIGHTBLUE,self.show_start_screen)
            pygame.display.flip()
            height = 0

    # ---------------- Other Functions ----------------

    def unpause(self):
        # Unpause the game
        self.pause = False
        pygame.mixer.music.unpause()

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
            smallText = pygame.font.SysFont(None,20)
            textSurf, textRect = self.text_objects(msg, smallText)
            textRect.center = ( (x+(w/2)), (y+(h/2)) )
            self.screen.blit(textSurf, textRect)
            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(self.screen, ic,(x,y,w,h))
            smallText = pygame.font.SysFont(None,20)
            textSurf, textRect = self.text_objects(msg, smallText)
            textRect.center = ( (x+(w/2)), (y+(h/2)) )
            self.screen.blit(textSurf, textRect)

    def quit_game(self):
        # Close the Game
        pygame.mixer.music.stop()
        pygame.quit()
        quit()

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()
quit()
