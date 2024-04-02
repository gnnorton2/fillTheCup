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
    
class Instructions(simpleGE.Scene):
    def __init__(self, pastScore):
        super().__init__()
        
        
        self.pastScore = pastScore
        
        
        self.setImage("bubbles.png")
        
        self.response = "Quit"
        
        self.howTo = simpleGE.MultiLabel()
        self.howTo.textLines = [
            "You just got a job at EcDonald's.",
            "Somebody mixed up all the spicy water.",
            "",
            "Move with the left and right arrow keys",
            "to fill the customer's cup with",
            "the correct spicy water.",
            "",
            "Here at EcDonald's, we Sprit, Ciera Missed,",
            "7 Down, but NEVER Mountain Don't.",
            "",
            "Catch as much crisp spicy water as you can",
            "before time runs out."
            ]
        self.howTo.center = (320, 215)
        self.howTo.size = (600, 400)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 450)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540, 450)
        
        self.pastScoreLabel = simpleGE.Label()
        self.pastScoreLabel.text = "Last Score: 0"
        self.pastScoreLabel.center = (320, 450)
    
        self.pastScoreLabel.text = f"Last score: {self.pastScore}"
        
        self.sprites = [self.howTo,
                        self.btnPlay,
                        self.btnQuit,
                        self.pastScoreLabel]
        
    
        
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
            
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
    
    
def main():
    keepGoing = True
    lastScore = 0
    while keepGoing:
       
        instructions = Instructions(lastScore)
        
        instructions.start()
      #  print(instructions.response)
    
        if instructions.response == "Play":    
            game = Game()
            game.start()
            lastScore = game.score
        else:
            keepGoing = False

if __name__ == "__main__":
    main()