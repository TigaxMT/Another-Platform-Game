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
from widgets import *
from screens import *

class Game:
    def __init__(self):
        # Initialize game window, mixer, clock etc

        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.widgets = Widgets(self.screen)
        self.screens = Screens(self,self.screen,self.widgets)

        imgIcon = pygame.image.load(PLAYER_IMAGE_LIST_RIGHT[2]).convert_alpha()
        pygame.display.set_icon(imgIcon)
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
        self.assets = pygame.sprite.Group()
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
        keys = pygame.key.get_pressed()

        # ------------- Collisions ----------- #


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

        for plat in self.platforms:
            if self.player.rect.colliderect(plat.rect):
                if self.player.vel.y < 0: # Moving up; Hit the bottom side of the wall
                    self.player.rect.top = plat.rect.bottom
                    self.player.vel.y = 10

        # ------------- End of Collisions ----------- #

        # if player reaches WIDTH - 250

        if self.player.pos.x <= 0:
            self.player.pos.x = 0

        if self.player.rect.right >= (WIDTH - 250):
            self.player.pos.x -= abs(self.player.vel.x)

            # Only if the player moves to right platforms and assets move
            if keys[pygame.K_RIGHT]:
                for plat in self.platforms:
                    if self.player.vel.x > 0:
                        plat.rect.x -= abs(self.player.vel.x )
                    if plat.rect.right < 0:
                        plat.kill()

                for ass in self.assets:
                    if self.player.vel.x > 0:
                        ass.rect.x -= abs(self.player.vel.x )
                    if ass.rect.right < 0:
                        ass.kill()

                # Give the base platform movement for each platform
                for bases in self.base:
                    if self.player.vel.x > 0:
                        bases.rect.x -= abs(self.player.vel.x )
                    if bases.rect.right < 0:
                        bases.kill()
                    #Randomize base platforms
                    while len(self.base) < 2:
                        if bases.rect.right <= WIDTH:
                            b = Base(BASE[0], random.randrange(WIDTH,WIDTH + 50) , HEIGHT - 71)
                            self.base.add(b)
                            self.all_sprites.add(b)

        # Randomize platforms
        while len(self.platforms) < 1:
            p = Platform(random.randrange(WIDTH, WIDTH+250),
                            random.randrange(HEIGHT / 2,  HEIGHT - (71+71)),
                            195, 71)
            self.platforms.add(p)
            self.all_sprites.add(p)
        # Randomize assets
        while len(self.assets) < 2:
            n_img = random.randrange(0,len(ASSETS))
            
            #Load the image the Asset class will load to get the height for spawn correctly the assets
            img = pygame.image.load(ASSETS[n_img]).convert_alpha()
            height_img = img.get_size()[1]

            a = Asset(ASSETS[n_img],random.randrange(WIDTH,WIDTH+250),HEIGHT - (height_img+71))
            self.assets.add(a)
            self.all_sprites.add(a)

        # If player fall down
        if self.player.rect.bottom >= HEIGHT:
            self.screens.game_over()
    
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
                        self.screens.paused()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        # after drawing everything, flip the display
        pygame.display.flip()

    # ---------------- Screens Functions ----------------

            
    # ---------------- Other Functions ----------------
    
    def unpause(self):
        # Unpause the game
        self.pause = False
        pygame.mixer.music.unpause()

    def quit_game(self):
        # Close the Game
        pygame.mixer.music.stop()
        pygame.quit()
        quit()

g = Game()
g.screens.show_start_screen()
while g.running:
    g.new()

pygame.quit()
quit()
