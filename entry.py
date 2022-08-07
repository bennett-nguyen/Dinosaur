import time
import pygame as pg
import src.preload.ds as ds
import src.preload.constant as const

from sys import exit
from src.comp.scene.game import Game
from src.preload.shared import shared_data

main_game = Game()

dt: float = 0
current: float = 0
last: float = time.time()

while 1:
    current = time.time()
    dt = current - last
    last = current

    ds.screen.fill(main_game.screen_color)
    main_game.apply_color()
    ds.clock.tick(const.FPS)

    events = pg.event.get()
    shared_data.events = events
    shared_data.dt = dt

    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    main_game.update()
    pg.display.flip()