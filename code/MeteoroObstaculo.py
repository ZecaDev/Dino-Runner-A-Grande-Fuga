import pygame

from code.Entity import Entity


class MeteoroObstaculo(Entity):
    def __init__(self,name: str, position):
        super().__init__(name, position)
        self.speed = 10

    def move(self):
        self.rect.x -= self.speed