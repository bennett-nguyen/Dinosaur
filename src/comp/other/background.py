import pygame as pg
import src.preload.assets as assets
import src.preload.constant as const

from random import choice
from src.comp.export.star import Star
from src.comp.export.moon import Moon
from src.comp.export.cloud import Cloud
from src.preload.shared import shared_data, cache


class Background:
    def __init__(self):
        self.current_time = 0
        self.switched_state_time = 0
        self.switched_moon_phase = False
        self.moon = Moon()

        # Preallocate lists
        self.clouds: list[Cloud] = [0] * const.CLOUDS_AMOUNT
        self.stars: list[Star] = [0] * const.STARS_AMOUNT

        star_coords = ((68, 119), (349, 144), (107, 75), (478, 97), (274, 148), (908, 91), (1169, 87), (835, 68), (741, 81), (1179, 108))
        self.cloud_coords = ((2170, 108), (1657, 57), (1877, 137), (1304, 70), (1549, 65), (2013, 93))

        for i in range(const.CLOUDS_AMOUNT):
            surf = assets.Gallery.CLOUD
            rect = surf.current.get_rect(center=self.cloud_coords[i])
            cloud = Cloud(surf, rect, const.CLOUD_VELOCITY)
            self.clouds[i] = cloud

        for i in range(const.STARS_AMOUNT):
            surf = choice(assets.Gallery.STARS)
            if shared_data.time_state == const.DAY:
                surf.set_alpha(0)
            elif shared_data.time_state == const.NIGHT:
                surf.set_alpha(const.STAR_ALPHA)

            rect = surf.get_rect(center=star_coords[i])
            star = Star(surf, rect)
            self.stars[i] = star

    def draw_moon_n_stars(self):
        if shared_data.time_state == const.NIGHT and not self.switched_moon_phase:
            self.moon.index += 1
            self.switched_moon_phase = True
            if self.moon.index > len(self.moon.stages) - 1:
                self.moon.index = 0
        elif shared_data.time_state == const.DAY:
            self.switched_moon_phase = False
        self.moon.draw()

        for star in self.stars:
            star.draw()

    def move_clouds(self):
        for cloud in self.clouds:
            cloud.move()

    def draw_clouds(self):
        for cloud in self.clouds:
            cloud.draw()

    def reset(self):
        if cache.time_state == const.DAY:
            alpha = 0
            index = -1

        else:
            alpha = 255
            index = 0

        self.moon.index = index
        self.moon.alpha = alpha
        self.moon.surf.set_alpha(alpha)

        for star in self.stars:
            star.alpha = alpha
            star.image.set_alpha(alpha)

        for cloud, coords in zip(self.clouds, self.cloud_coords):
            cloud.rect.center = coords
