# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:59:25 2024

@author: gnoel
"""

import pygame, random, simpleGE

class EcDonalds(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("cup.png")
        self.position = (320, 400)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("bubbles.png")
        self.cup = EcDonalds(self)
        
        self.sprites = [self.cup]
        
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()