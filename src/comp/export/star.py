import pygame as pg
import src.preload.ds as ds
import src.preload.constant as const
from src.preload.shared import shared_data

class Star:
    def __init__(self, image: pg.Surface, rect: pg.Rect):
        self.image = image
        self.rect = rect
        self.alpha = const.STAR_ALPHA if shared_data.time_state == const.NIGHT else 0
        self.alpha_modifier = 270

    def change_alpha(self):
        modifier = round(self.alpha_modifier * shared_data.dt)
        if self.alpha > 0 and shared_data.time_state == const.DAY:
            self.alpha -= modifier
        elif self.alpha < const.STAR_ALPHA and shared_data.time_state == const.NIGHT:
            self.alpha += modifier
            self.alpha = min(self.alpha, const.STAR_ALPHA)

        self.image.set_alpha(self.alpha)

    def draw(self):
        self.change_alpha()
        if self.rect.left <= const.WIDTH:
            ds.screen.blit(self.image, self.rect)
