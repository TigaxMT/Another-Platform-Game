"""
    A simple platform game written in Python

    Copyright (C) 2017-2018  Tiago Martins, Kelvin Ferreira

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

from game_modules.settings.player import PlayerSettings
from game_modules.settings.sprites import PlayerSprites
from game_modules.settings.platform import PlatformSettings
from game_modules.settings.audio import GameAudios

vec = pygame.math.Vector2  # define a variable vectors for the movements

class Player(pygame.sprite.Sprite):  # Creates a Player Sprite
    def __init__(self, game):

        #Initialize the Sprite function
        pygame.sprite.Sprite.__init__(self)

        # Pass a game instance of Game Class for player to has access of the Game vars/funcs etc
        self.game = game

        #Define the stop player sprite and get the rectangle of him
        self.image = pygame.image.load(
            PlayerSprites.PLAYER_IMAGE_LIST_RIGHT[1])
        self.rect = self.image.get_rect()
        self.rect.center = (PlatformSettings.WIDTH / 2,
                            PlatformSettings.HEIGHT / 2)

        #Define the vectors of position , velocity and acceleration
        self.pos = vec(PlatformSettings.WIDTH / 2,
                       PlatformSettings.HEIGHT - 71)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        # Use 3 counter variables to know what image use
        self.counter_right = 0
        self.counter_left = 0
        self.counter_stopped = 0
        self.counter_attack = -1

        # direc variable is use for set the player direction when it is stopped
        self.direc = "right"

        #Jump sound
        self.jump_sound = pygame.mixer.Sound(GameAudios.PLAYER_JUMP)
        self.jump_sound.set_volume(0.6)

        #Sword sound
        self.sword_sound = pygame.mixer.Sound(GameAudios.SWORD)
        self.sword_sound.set_volume(0.6)

        #Enemy Die sound
        self.enemy_die_sound = pygame.mixer.Sound(GameAudios.ENEMY_DIE)
        self.enemy_die_sound.set_volume(0.6)

    def jump(self):  # jump only if standing on a platform
        #Increment the player rectangle position for a better collision detection
        self.rect.x += 1

        #Verify if player hits a platform or a base
        hits = pygame.sprite.spritecollide(self, self.game.level.platforms, False)
        hits_base = pygame.sprite.spritecollide(self, self.game.level.base, False)

        #Decrement the player rectangle position for the initial position

        #If it stand in a platform or a base, the y velocity is decremented
        self.rect.x -= 1
        if hits:
            self.vel.y = -20
            pygame.mixer.Sound.play(self.jump_sound)

        elif hits_base:
            self.vel.y = -20
            pygame.mixer.Sound.play(self.jump_sound)    
            
    def sword_attack(self):
        
        # Only plays sword sound if the Space Key was pressed
        
        if self.counter_attack == 0:
            pygame.mixer.Sound.play(self.sword_sound)
            
         # Animation of player attack
        if self.direc == 'left':
            
           # Verify if is the last image of the sprite animation, if it was restart the counter
            if self.counter_attack == 8:
                self.counter_attack = -1
            
            else:
                #Update the player image with the correct image, to give the sensation of movement
                self.image = pygame.image.load(
                        PlayerSprites.PLAYER_IMAGE_ATTACK_LEFT[self.counter_attack]).convert_alpha()
            
                self.counter_attack += 1
            
                self.game.draw()
                
                pygame.time.delay(25)

        else:
           
            # Verify if is the last image of the sprite animation, if it was restart the counter
            if self.counter_attack == 8:
                self.counter_attack = -1
            else:
                
                #Update the player image with the correct image, to give the sensation of movement
                self.image = pygame.image.load(
                    PlayerSprites.PLAYER_IMAGE_ATTACK_RIGHT[self.counter_attack]).convert_alpha()
                
                self.counter_attack += 1
                
                self.game.draw()
                
                pygame.time.delay(25)
    
        # Verify if player hit an enemy with the sword attack, if yes the enemy will be killed
        if self.pos.y == PlatformSettings.HEIGHT - 71:
            for enm in self.game.level.enemies:
                if self.direc == 'right' and (enm.rect.x - self.rect.x) <= 55 and (enm.rect.x - self.rect.x) >= 1:
                    self.game.level.score += 1
                    self.game.level.max_enemies += 1
                    pygame.mixer.Sound.play(self.enemy_die_sound)
                    enm.kill()
                elif self.direc == 'left' and (self.rect.x - enm.rect.x) <= 55 and (self.rect.x - enm.rect.x) >= 1:
                    self.game.level.score += 1
                    self.game.level.max_enemies += 1
                    pygame.mixer.Sound.play(self.enemy_die_sound)
                    enm.kill()
    
    def collisionDetection(self):

        keys = pygame.key.get_pressed()

        # check if player collide a platform or an enemy when it's falling
        if self.vel.y > 0:
            for plat in self.game.level.platforms:
                if self.rect.colliderect(plat.rect):
                    if self.rect.bottom >= plat.rect.top:
                        self.pos.y = plat.rect.top
                        self.vel.y = 0

            for bas in self.game.level.base:
                if self.rect.colliderect(bas.rect):
                    if self.rect.bottom >= bas.rect.top:
                        self.pos.y = bas.rect.top
                        self.vel.y = 0

            # If player collide an enemy when it's falling , enemy will die

            if round(self.vel.y) > 0:
                for enm in self.game.level.enemies:
                    if self.rect.colliderect(enm.rect):
                        if self.rect.midbottom >= plat.rect.midtop:
                            pygame.mixer.Sound.play(self.enemy_die_sound)
                            self.vel.y = 0
                            self.vel.y = -15
                            self.game.level.score += 1
                            self.game.level.max_enemies += 1
                            enm.kill()



        # check if player collide an enemy when it's running

        if self.pos.y == PlatformSettings.HEIGHT - 71:
            for enm in self.game.level.enemies:
                if self.rect.colliderect(enm.rect):        
                    if self.rect.right >= enm.rect.left:
                        
                        for i in range(0,8):
                            self.image = pygame.image.load(
                                        PlayerSprites.PLAYER_IMAGE_DEAD[i]).convert_alpha()
                            self.game.draw()
                            pygame.time.delay(100)
                            
                        self.game.screen.game_over()

                    elif self.rect.left <= enm.rect.right:
                        
                        for i in range(0,8):
                            self.image = pygame.image.load(
                                        PlayerSprites.PLAYER_IMAGE_DEAD[i]).convert_alpha()
                            
                            self.game.draw()
                            pygame.time.delay(100)
                            
                        self.game.screen.game_over()



        # check if player collide a platform when it's running

        if round(self.vel.x) != 0 and self.pos.y == PlatformSettings.HEIGHT - 71:

            for plat in self.game.level.platforms:
                if self.rect.colliderect(plat.rect):
                    
                    if self.rect.midright >= plat.rect.midleft and self.rect.midright < plat.rect.midright and keys[pygame.K_RIGHT]:
                        self.pos.x = plat.rect.left
                        self.pos.y = PlatformSettings.HEIGHT - 71
                        self.vel.x = 0
                        self.acc.x = 0
                        self.game.level.side_collide = True
                    
                    elif self.rect.midleft <= plat.rect.midright and self.rect.midleft > plat.rect.midleft and keys[pygame.K_LEFT]:
                        self.pos.x = plat.rect.right
                        self.pos.y = PlatformSettings.HEIGHT - 71
                        self.vel.x = 0
                        self.acc.x = 0
                        self.game.level.side_collide = True
                    
                    else:
                        self.game.level.side_collide = False
                else:
                    self.game.level.side_collide = False

    def update(self):  # Update Sprites on the screen

        #Define acceleration with the gravity constant (defined in settings script)
        self.acc = vec(0, PlayerSettings.PLAYER_GRAV)

        #Store all the keys pressed
        keys = pygame.key.get_pressed()
        
        #Verify if attack ended , if not execute the function
        
        if self.counter_attack != -1:
            
            self.sword_attack()
        
        #If Space bar pressed
        if keys[pygame.K_SPACE]:
            self.counter_attack = 0
            self.sword_attack()
        
        #If left key pressed
        if keys[pygame.K_LEFT]:

            # Verify if is the last image of the sprite animation, if it was restart the counter
            if self.counter_left == 8:
                self.counter_left = 0

            #Update the player image with the correct image, to give the sensation of movement
            self.image = pygame.image.load(
                PlayerSprites.PLAYER_IMAGE_LIST_LEFT[self.counter_left]).convert_alpha()

            #Put an negative(oposite for the right movement) constant acceleration to the player to give better physics
            self.acc.x = -PlayerSettings.PLAYER_ACC

            self.counter_left += 1
            self.direc = 'left'

        #If right key pressed
        if keys[pygame.K_RIGHT]:
            # Verify if is the last image of the sprite animation, if it was restart the counter
            if self.counter_right == 8:
                self.counter_right = 0

            #Update the player image with the correct image, to give the sensation of movement
            self.image = pygame.image.load(
                PlayerSprites.PLAYER_IMAGE_LIST_RIGHT[self.counter_right]).convert_alpha()

            #Put an positive(oposite for the left movement) constant acceleration to the player to give better physics
            self.acc.x = PlayerSettings.PLAYER_ACC

            self.counter_right += 1
            self.direc = 'right'
        
        if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            
            for i in range(0,8):
                
                    self.image = pygame.image.load(
                    PlayerSprites.PLAYER_IMAGE_BACKFLIP[i]).convert_alpha()

                    self.game.draw()
                    pygame.time.delay(50)
            
            #Put an negative(oposite for the right movement) constant acceleration to the player to give better physics
            self.acc.x = -PlayerSettings.PLAYER_ACC
            
            self.direc = 'right'

        # apply friction to the acceleration
        self.acc.x += self.vel.x * PlayerSettings.PLAYER_FRICTION

        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

        # Set the Player Sprite Animation Stopped
        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            if self.counter_stopped == 9:
                self.counter_stopped = 0

            self.image = pygame.image.load(
                PlayerSprites.PLAYER_IMAGE_STOPPED[self.counter_stopped]).convert_alpha()
            self.counter_stopped += 1
        else:
            self.counter_stopped = 0
