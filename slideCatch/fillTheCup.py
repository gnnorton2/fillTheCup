# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:59:25 2024

@author: gnoel
"""

import pygame, random, simpleGE

def main():
    
    
    #Important and Initialize Idea
    #already imported
    pygame.init()
    
    #iDea Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Fill the Cup")
    
    #idEa background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background = pygame.image.load("bubbles.png")
    
    clock = pygame.time.Clock()
    keepGoing = True
    
    #aLter loop
    while keepGoing:
        
        #alTer Timer
        clock.tick(30) #fps
        
        #altEr Event haandling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
    
    #alteR refresh
        screen.blit(background, (0, 0))
        pygame.display.flip()
    
class EcDonalds(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("youveGotMail") #CHANGE THIS LATER ONCE WORKING
        self.setSize(50, 50)
        


if __name__ == "__main__":
    main()