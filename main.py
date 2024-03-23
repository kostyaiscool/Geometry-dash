import pygame as pg

import level
from config import WIDTH, HEIGHT
from player import Player
from level import level

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

def run():
    game = True
    color = (66, 93, 245)
    player = Player()
    while game:
        screen.fill(color)
        player.show_player(screen)
        player.jump()
        for i in level:
            i.show_image(screen)
            i.move()
            if player.rect.colliderect(i.rect):
                player.collisions(i)
        pg.display.update()
        clock.tick(60)
        events = pg.event.get()
        for e in events:
            if e.type == pg.QUIT:
                game = False
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_UP or e.key == pg.K_SPACE:
                    if player.jumpcount == player.jumppower:
                        player.jumps = True
            if e.type == pg.MOUSEBUTTONDOWN:
                if player.jumpcount == player.jumppower:
                    player.jumps = True


run()