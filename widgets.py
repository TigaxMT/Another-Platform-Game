from settings import *
import pygame

class Widgets:
    def __init__(self,screen):
        self.screen = screen
    
    def text_objects(self,text, font,color=BLACK):
        # Creates Text Messages
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def button(self,msg,x,y,w,h,ic,ac,action=None):
        # Create Buttons
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.screen, ac,(x,y,w,h))
            smallText = pygame.font.SysFont(None,20)
            textSurf, textRect = self.text_objects(msg, smallText,BLACK)
            textRect.center = ( (x+(w/2)), (y+(h/2)) )
            self.screen.blit(textSurf, textRect)
            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(self.screen, ic,(x,y,w,h))
            smallText = pygame.font.SysFont(None,20)
            textSurf, textRect = self.text_objects(msg, smallText,BLACK)
            textRect.center = ( (x+(w/2)), (y+(h/2)) )
            self.screen.blit(textSurf, textRect)