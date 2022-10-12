import sys
import pygame as pg

def process_events(game):
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            sys.exit()