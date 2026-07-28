import pygame
class Time:
    deltaTime = 0.02
    def __init__(self):
        self.clock=pygame.time.Clock()
    def Tick(self):
        self.clock.tick(60)
