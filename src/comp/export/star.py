import pygame as pg
import src.preload.ds as ds
import src.preload.constant as const

class Star:
    def __init__(self, image: pg.Surface, rect: pg.Rect, time_state: str):
        self.image = image
        self.rect = rect
        self.alpha = const.STAR_ALPHA
        self.time_state = time_state

    def change_alpha(self):
        if self.alpha > 0 and self.time_state == 'day':
            self.alpha -= 3
        elif self.alpha < const.STAR_ALPHA and self.time_state == 'night':
            self.alpha += 3
            self.alpha = min(self.alpha, const.STAR_ALPHA)

        self.image.set_alpha(self.alpha)

    def draw(self):
        self.change_alpha()
        if self.rect.left <= const.WIDTH:
            ds.screen.blit(self.image, self.rect)