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
from settings import * # constants
from sprites import * # sprites
from widgets import * # buttons and texts
from screens import * # credits , gameover, pause screens


class Game:
    def __init__(self): # Initialize game window, mixer, clock etc

        #Initialize the mixer
        pygame.init()
        pygame.mixer.init()

        #Create a surface
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        #Define and initialize classes objects
        self.widgets = Widgets(self.screen)
        self.screens = Screens(self,self.screen,self.widgets)

        #Change the game icon and title
        imgIcon = pygame.image.load(PLAYER_IMAGE_LIST_RIGHT[2]).convert_alpha()
        pygame.display.set_icon(imgIcon)
        pygame.display.set_caption(TITLE)

        #Create and define already the main sprite group
        self.all_sprites = pygame.sprite.Group()
        
        #Define and initialize clock and boolean pause to know if game is paused or not
        self.clock = pygame.time.Clock()
        self.pause = False

        #Variable to store FPS
        self.fps = 0.0

        #Define and initialize with random data the variable to manipulate and Draw Text Objects
        self.smallText = pygame.font.SysFont(None,40)
        self.textSurf, textRect = self.widgets.text_objects("FPS: " + str(self.fps), self.smallText,BLACK)

    def new(self): # Start a new game

        # Kill all sprites if they exists
        if len(self.all_sprites) != 0:
            self.killAllSprites()

        #Loading and playing the main soundtrack
        pygame.mixer.music.load(MUSIC[0])
        pygame.mixer.music.play(-1)

        #Define a object to Player Class (sprite player class) 
        self.player = Player(self)

        #Create all needed sprite groups
        self.platforms = pygame.sprite.Group()
        self.assets = pygame.sprite.Group()
        self.base = pygame.sprite.Group()

        #Define the first platform_base position
        b = Base(BASE[0],0 , HEIGHT-71)
        self.base.add(b)
        
        #Define the background image(sprite)
        self.background = Background(BG[0], [0,0])
        
        #Add to the main sprite group all the others sprite groups
        self.all_sprites.add(self.background)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.base)

        #Call the main loop function
        self.run()

    def run(self): # Game Loop
        
        self.playing = True
        
        # Main Loop
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self): # Game Loop - Update

        self.all_sprites.update()

        #Get all keys pressed
        keys = pygame.key.get_pressed()

        # check if player collide a platform when it's falling
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            hits_base = pygame.sprite.spritecollide(self.player, self.base, False)
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
                    if self.player.vel.y < 0: # Moving up; Hit the bottom side of the wall
                        self.player.rect.top = plat.rect.bottom
                        self.player.vel.y = 10


        # if player reaches 0 width, platforms and assets stop moving

        if self.player.pos.x <= 0:
            self.player.pos.x = 0

        # if player reaches WIDTH - 250 , player stay running in the same position (WIDTH - 250)
        if self.player.rect.right >= (WIDTH - 250):
            self.player.pos.x -= abs(self.player.vel.x)

            # Only if the player moves to right, platforms and assets move
            if keys[pygame.K_RIGHT]:
                
                #Moving each platform and kill platforms reach Width 0
                for plat in self.platforms:
                    if self.player.vel.x > 0:
                        plat.rect.x -= abs(self.player.vel.x )
                    if plat.rect.right < 0:
                        plat.kill()

                #Moving each asset and kill assets reach Width 0
                for ass in self.assets:
                    if self.player.vel.x > 0:
                        ass.rect.x -= abs(self.player.vel.x )
                    if ass.rect.right < 0:
                        ass.kill()

                #Moving each base and kill bases reach Width 0
                for bases in self.base:
                    if self.player.vel.x > 0:
                        bases.rect.x -= abs(self.player.vel.x )
                    if bases.rect.right < 0:
                        bases.kill()

                    #Randomize base platforms,only if don't have 2 bases spawned
                    while len(self.base) < 2:
                        if bases.rect.right <= WIDTH:
                            b = Base(BASE[0], random.randrange(WIDTH,WIDTH + 50) , HEIGHT - 71)
                            self.base.add(b)
                            self.all_sprites.add(b)

        # Randomize platforms, only if don't have 1 spawned
        while len(self.platforms) < 1:
            p = Platform(random.randrange(WIDTH, WIDTH+250),
                            random.randrange(HEIGHT / 2,  HEIGHT - (71+71)),
                            195, 71)
            self.platforms.add(p)
            self.all_sprites.add(p)

        # Randomize assets, only if don't have 2 assets spawned
        while len(self.assets) < 2:
            n_img = random.randrange(0,len(ASSETS))
            
            #Load the image: the Asset class will load to get the height for spawn correctly the assets
            img = pygame.image.load(ASSETS[n_img]).convert_alpha()
            height_img = img.get_size()[1]

            #Define a class Asset object and add it to the main sprite group 
            a = Asset(ASSETS[n_img],random.randrange(WIDTH,WIDTH+250),HEIGHT - (height_img+71))
            self.assets.add(a)
            self.all_sprites.add(a)

        # If player fall down
        if self.player.rect.bottom >= HEIGHT:
            self.screens.game_over()
    
    def events(self): # Game Loop - events

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
                        self.screens.paused()

    def draw(self): # Game Loop - draw

        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)

        #Draw FPS
        self.showFPS()

        # after drawing everything, flip(update) the display
        pygame.display.flip()
      

    def showFPS(self): # Show FPS on screen

        #Update FPS variable
        self.fps = round(self.clock.get_fps())
        
        #Create and draw a surface and rectangle for the FPS text
        self.smallText = pygame.font.SysFont(None,40)
        self.textSurf, self.textRect = self.widgets.text_objects("FPS: " + str(self.fps), self.smallText,BLACK)
        self.textRect.x = 30
        self.textRect.y = 30
        self.screen.blit(self.textSurf, self.textRect)

    def killAllSprites(self): #Kill all Sprites

        self.all_sprites.empty()
        self.platforms.empty()
        self.assets.empty()
        self.base.empty()

    def unpause(self): # Unpause the game

        self.pause = False
        pygame.mixer.music.unpause()

    def quit_game(self): # Close the Game
        
        pygame.quit()
        quit()

# Create an Object of the Game Class
g = Game()

#Call the start screen funcion
g.screens.show_start_screen()