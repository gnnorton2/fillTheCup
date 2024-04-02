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
   
class ScoreLabel(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)

class TimeLabel(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left: 10"
        self.center = (530, 30)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("bubbles.png")
        
        self.sndSprit = simpleGE.Sound("spicywater.wav")
        
        numSprits = 10
        
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.timeLabel = TimeLabel()
        
        self.scoreLabel = ScoreLabel()
        self.score = 0
        
        self.ecup = EcDonalds(self)
        
        self.sprits = []
        for i in range(numSprits):
            self.sprits.append(Sprit(self))
            
        self.sprites = [self.ecup, 
                        self.sprits,
                        self.scoreLabel,
                        self.timeLabel]
    
    
    
    def process(self):
        for sprit in self.sprits:
            if sprit.collidesWith(self.ecup):
                sprit.reset()
                self.sndSprit.play()
                self.score += 1
                self.scoreLabel.text = f"Score: {self.score}"
                
        self.timeLabel.text = f"Time left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()
    
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()