import pygame as pg
import src.preload.ds as ds
from src.preload.shared import shared_data
import src.preload.constant as const
from src.preload.comp import ImageState

class Cloud:
    def __init__(self, image: ImageState, rect: pg.Rect, velocity: int):
        self.image = image
        self.rect = rect
        self.velocity = velocity

    def move(self):
        rect_x = self.rect.x
        rect_x -= round(self.velocity * shared_data.dt)
        self.rect.x = rect_x
        if self.rect.right <= 0:
            self.rect.left = const.WIDTH

    def draw(self):
        if self.rect.left <= const.WIDTH:
            self.image.get_state(shared_data.time_state)
            ds.screen.blit(self.image.current, self.rect)