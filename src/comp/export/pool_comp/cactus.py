import pygame as pg
import src.preload.ds as ds
import src.preload.constant as const
from src.preload.comp import ImageState
from src.preload.shared import shared_data


class Cactus:
    def __init__(self, images: list[ImageState]):
        self.__init_surface(images)
        self.__draw_cactus(images)
        self.images = images
        self.is_standalone_object = len(images) == 1
        self.x = const.WIDTH + 100
        self.rect = self.image.current.get_rect(midbottom=(self.x, shared_data.GROUND_Y_VALUE))
        self.id = const.CACTUS

    def move(self):
        self.rect.x -= shared_data.velocity

    def redraw(self):
        self.image.get_state(shared_data.time_state)
        ds.screen.blit(self.image.current, self.rect)

    def __init_surface(self, images: list[ImageState]):
        width, height = 0, 0
        for image in images:
            height = max(height, image.current.get_height())
            width += image.current.get_width() + 5 # 5 for some spacing between each cactus

        self.day_surf = pg.Surface((width, height), pg.SRCALPHA, 32)
        self.night_surf = pg.Surface((width, height), pg.SRCALPHA, 32)

    def __draw_cactus(self, images: list[ImageState]):
        pos_x = 0
        for image in images:
            self.day_surf.blit(image.day_image.copy(), (pos_x, 0))
            self.night_surf.blit(image.night_image.copy(), (pos_x, 0))
            pos_x += image.current.get_width() + 5 # 5 for some spacing between each cactus

        self.image = ImageState(self.day_surf, self.night_surf)
        delattr(self, 'day_surf')
        delattr(self, 'night_surf')
    
    def change_pos(self, x: int):
        self.rect.centerx = x
        self.rect.bottom = shared_data.GROUND_Y_VALUE