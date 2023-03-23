import pygame as pg
from src.preload.settings import *


class Star:
    def __init__(self, game, image: pg.Surface, rect: pg.Rect):
        self.game = game

        # Images
        self.image = image
        self.rect = rect

        # Transparency
        self.alpha = STAR_ALPHA if self.game.time_state == NIGHT else 0
        self.alpha_modifier = 270

    def change_alpha(self):
        modifier = round(self.alpha_modifier * self.game.delta_time)

        if self.alpha > 0 and self.game.time_state == DAY:
            self.alpha -= modifier
        elif self.alpha < STAR_ALPHA and self.game.time_state == NIGHT:
            self.alpha += modifier
            self.alpha = min(self.alpha, STAR_ALPHA)

        self.image.set_alpha(self.alpha)

    def draw(self):
        self.change_alpha()
        self.game.screen.blit(self.image, self.rect)
