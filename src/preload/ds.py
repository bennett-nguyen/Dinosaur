import pygame as pg
from pygame.locals import QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, WINDOWFOCUSLOST, WINDOWMOVED
import src.preload.constant as const

pg.mixer.pre_init(44100, -16, 2, 512)
pg.init()


pg.event.set_allowed([QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, WINDOWFOCUSLOST, WINDOWMOVED])
pg.display.set_caption("Python Dinosaur")

clock = pg.time.Clock()
screen = pg.display.set_mode((const.WIDTH, const.HEIGHT))

__ICON = pg.image.load('./assets/img/icon/dino.ico').convert_alpha()
pg.display.set_icon(__ICON)