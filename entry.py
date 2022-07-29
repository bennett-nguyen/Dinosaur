import time
import pygame as pg
import src.preload.ds as ds
import src.preload.constant as const
from src.preload.shared import shared_data

from sys import exit
from src.comp.scene.game import Game

main_game = Game()


dt = 0
current = 0
last = time.time()
while True:
    current = time.time()
    dt = current - last
    last = current

    ds.screen.fill(main_game.screen_color)
    main_game.apply_color()
    ds.clock.tick(const.FPS)

    events = list(pg.event.get())
    shared_data.events = events
    shared_data.dt = dt

    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            exit()
            
    main_game.update()
    pg.display.update()