# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:59:25 2024

@author: gnoel
"""

import pygame, random, simpleGE


    
class Blast(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("brBlast.png")
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

class Mtn(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("mtnDont.png")
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
    
class Seven(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("sevenDown.png")
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

class Ciera(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("cieraMissed.png")
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
        if self.isKeyPressed(pygame.K_a):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_d):
            self.x += self.moveSpeed
            
   
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
        self.sndCiera = simpleGE.Sound("spicywater.wav")
        self.sndSeven = simpleGE.Sound("spicywater.wav")
        self.sndMtn = simpleGE.Sound("ew.wav")
        self.sndBlast = simpleGE.Sound("freeze.wav")
        #add brblast sound
        self.sndRick = simpleGE.Sound("roll.wav")
        
        numSprits = 3
        numCieras = 3
        numSevens = 2
        numMtns = 3
        numBlasts = 1
        
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.timeLabel = TimeLabel()
        
        self.scoreLabel = ScoreLabel()
        self.score = 0
        
                
                
        
        self.ecup = EcDonalds(self)
        
        self.sprits = []
        for i in range(numSprits):
            self.sprits.append(Sprit(self))
            
        self.cieras = []
        for i in range(numCieras):
            self.cieras.append(Ciera(self))
            
        self.sevens = []
        for i in range(numSevens):
            self.sevens.append(Seven(self))
            
        self.mtns = []
        for i in range(numMtns):
            self.mtns.append(Mtn(self))
            
        self.blasts = []
        for i in range(numBlasts):
            self.blasts.append(Blast(self))
            
        
            
        self.sprites = [self.ecup, 
                        self.sprits,
                        self.cieras,
                        self.sevens,
                        self.mtns,
                        self.blasts,
                        self.scoreLabel,
                        self.timeLabel]
    
    
    
    def process(self):
        for sprit in self.sprits:
            if sprit.collidesWith(self.ecup):
                sprit.reset()
                self.sndSprit.play()
                self.score += 1
                self.scoreLabel.text = f"Score: {self.score}"
                
        for ciera in self.cieras:
            if ciera.collidesWith(self.ecup):
                ciera.reset()
                self.sndCiera.play()
                self.score += 1
                self.scoreLabel.text = f"Score: {self.score}"
                
        for seven in self.sevens:
            if seven.collidesWith(self.ecup):
                seven.reset()
                self.sndSeven.play()
                self.score += 1
                self.scoreLabel.text = f"Score: {self.score}"
                
        for mtn in self.mtns:
            if mtn.collidesWith(self.ecup):
                mtn.reset()
                self.sndMtn.play()
                self.score -= 1
                self.scoreLabel.text = f"Score: {self.score}"
                self.timer.totalTime -= 2
        
        for blast in self.blasts:
            if blast.collidesWith(self.ecup):
                blast.reset()
                self.sndBlast.play()
                self.timer.totalTime += 3
                #self.scoreLabel.text = f"Score: {self.score}"
        
        
                
        self.timeLabel.text = f"Time left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()
            
        if self.score == 15:
            self.sndRick.play()
            self.setImage("rick.png")
            self.timer.start()
            if self.score == 50:
                self.sndRick.play()
                self.timer.start()
                
                
            
    
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