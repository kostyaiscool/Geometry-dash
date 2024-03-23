import sys

import pygame as pg
from config import WIDTH, HEIGHT
import level

X = WIDTH / 2.3
Y = HEIGHT / 1.75
GRAVITY = 5.5

class Player(pg.sprite.Sprite):
    def __init__(self):
        self.gamemode = 'cube'
        self.speed = 20
        self.change_gamemode()
        self.rect = self.skin.get_rect()
        self.rect.x = X
        self.rect.y = Y
        self.speed_y = GRAVITY
        self.jumps = False
        self.jumppower = 20
        self.jumpcount = self.jumppower
        self.g = self.jumppower * 0.5

    def set_gamemode(self, gamemode):
        self.gamemode = gamemode
        self.change_gamemode()

    def change_gamemode(self):
        if self.gamemode == 'cube':
            self.skin = pg.image.load('Sources/Cube004.png')
            self.skin = pg.transform.scale(self.skin, (60, 60))
        elif self.gamemode == 'mini cube':
            pass
        elif self.gamemode == 'ship':
            pass
        elif self.gamemode == 'UFO':
            pass
        elif self.gamemode == 'ball':
            pass
        elif self.gamemode == 'wave':
            pass
        elif self.gamemode == 'robot':
            pass
        elif self.gamemode == 'spider':
            pass
        elif self.gamemode == 'swingcopter':
            pass
        elif self.gamemode == 'jetpack':
            pass

    def show_player(self, screen):
        screen.blit(self.skin, (self.rect.x, self.rect.y))

    def jump(self):
        if self.jumps and self.jumpcount != 0:
            self.rect.y -= self.speed_y + self.g
            self.g -= 0.5
            self.jumpcount -= 1
            print(self.g)
        elif self.jumps != True and self.jumpcount < self.jumppower:  #self.rect.y <= HEIGHT * 0.6:
            self.rect.y += self.speed_y + self.g
            self.g += 0.5
            self.jumpcount += 1
            print(self.g)
        # if self.rect.y <= HEIGHT * 0.5:
            # self.jumps = False
        if self.jumpcount == 0:
            self.jumps = False
    def collisions(self, touched_object):
        touched_object.collision()