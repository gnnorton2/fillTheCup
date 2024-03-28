# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:59:25 2024

@author: gnoel
"""

import pygame, random, simpleGE

class Sprit(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("sprit.png")
        self.minSpeed = 2
        self.maxSpeed = 9
        
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
       #speed
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
     
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            

class EcDonalds(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("ecup.png")
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            #add A and D later
            

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("bubbles.png")
        
        self.sndSprit = simpleGE.Sound("spicywater.wav")
        self.ecup = EcDonalds(self)
        self.sprit = Sprit(self)
        self.sprites = [self.ecup, 
                        self.sprit]
    
    def process(self):
        if self.sprit.collidesWith(self.ecup):
            self.sprit.reset()
            self.sndSprit.play()
    
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()