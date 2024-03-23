import sys
from abc import ABC, abstractmethod
import pygame as pg
from config import *


class Obstacle:
    '''этот клас являетца базовым длйа фсех фигур'''
    def __init__(self, image, x, y):
        self.speed = 7
        self.skin = pg.image.load(image)
        self.skin = pg.transform.scale(self.skin, (60, 60))
        self.rect = self.skin.get_rect()
        self.rect.x = x
        self.rect.y = y
    def show_image(self, screen):
        screen.blit(self.skin, (self.rect.x, self.rect.y))
    def move(self):
        self.rect.x -= self.speed

class Air(Obstacle):
    '''Ето клас являеца описанием для клеточек пустово пространстга и не имейет функции колизийи'''


#     @abstractmethod
#     def collisions(self):
#         pass

class Spike(Obstacle):
    def collision(self):
        sys.exit()

class Floor(Obstacle):
    ''''''
    def collision(self):
        pass

test = Spike('Sources/Spike.png', WIDTH / 0.5, HEIGHT / 1.85)
level = [test]