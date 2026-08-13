import pygame
class Time:
    deltaTime = 1/60
    def __init__(self):
        self.clock=pygame.time.Clock()
    def Tick(self):
        pass
        self.clock.tick_busy_loop(60)
