import pygame as pg
import src.preload.ds as ds
import src.preload.assets as assets
import src.preload.constant as const
from src.preload.comp import ImageState
from src.preload.shared import shared_data


class Cactus:
    def __init__(self, images: list[ImageState]):
        self.__init_surface(images)
        self.__draw_cactus(images)
        self.images = images
        self.is_standalone_object = len(images) == 1
        self.id = 'cactus'

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

    def init_pos(self, x: int):
        self.rect = self.image.current.get_rect(midbottom=(x, shared_data.GROUND_Y_VALUE))

one_small_cactus = [assets.Gallery.SMALL_CACTUS_1]
two_small_cacti = [assets.Gallery.SMALL_CACTUS_1, assets.Gallery.SMALL_CACTUS_2]
three_small_cacti = [assets.Gallery.SMALL_CACTUS_1, assets.Gallery.SMALL_CACTUS_4, assets.Gallery.SMALL_CACTUS_3]

one_big_cactus = [assets.Gallery.BIG_CACTUS_1]
two_big_cacti = [assets.Gallery.BIG_CACTUS_2, assets.Gallery.BIG_CACTUS_3]
three_big_cacti = [assets.Gallery.BIG_CACTUS_2, assets.Gallery.BIG_CACTUS_WITH_SMALL_CACTUS, assets.Gallery.BIG_CACTUS_4]

cacti = (one_small_cactus, two_small_cacti, three_small_cacti, one_big_cactus, two_big_cacti, three_big_cacti)