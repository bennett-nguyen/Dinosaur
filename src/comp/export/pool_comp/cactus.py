import pygame as pg
from typing import List
from src.preload.settings import *
from src.preload.utilities import ImageState


class Cactus:
    def __init__(self, game, images: List[ImageState]):
        self._init_surface(images)
        self._draw_cactus(images)
        self.game = game

        self.is_standalone_object = len(images) == 1
        self.rect = self.image.current.get_rect(midbottom=(WIDTH + 100, self.game.background.object_y))
        self.id = CACTUS

    def move(self):
        self.rect.x -= self.game.modifier.dino_velocity

    def redraw(self):
        self.image.get_state(self.game.time_state)
        self.game.screen.blit(self.image.current, self.rect)

    def _init_surface(self, images: List[ImageState]):
        width, height = 0, 0
        for image in images:
            height = max(height, image.current.get_height())
            width += image.current.get_width() + 5  # 5 for some spacing between each cactus

        self.day_surf = pg.Surface((width, height), pg.SRCALPHA, 32)
        self.night_surf = pg.Surface((width, height), pg.SRCALPHA, 32)

    def _draw_cactus(self, images: List[ImageState]):
        pos_x = 0
        for image in images:
            self.day_surf.blit(image.day_image.copy(), (pos_x, 0))
            self.night_surf.blit(image.night_image.copy(), (pos_x, 0))
            pos_x += image.current.get_width() + 5  # 5 for some spacing between each cactus

        self.image = ImageState(self.day_surf, self.night_surf, True)
        delattr(self, 'day_surf')
        delattr(self, 'night_surf')

    def change_pos(self, x: int):
        self.rect.centerx = x
        self.rect.bottom = self.game.background.object_y
