import pygame as pg
import src.preload.ds as ds
import src.preload.assets as assets
import src.preload.constant as const
from random import randint
from src.preload.shared import shared_data

class Pteranodon:
    def __init__(self):
        self.animation = [assets.Gallery.PTERANODON_FLYING_1, assets.Gallery.PTERANODON_FLYING_2]
        self.image = self.animation[0]
        self.is_standalone_object = True
        self.index = 0
        self.animation_speed = 6
        self.id = const.PTERANODON
        x = const.WIDTH + 200
        y = randint(shared_data.GROUND_Y_VALUE - 100, shared_data.GROUND_Y_VALUE)
        self.rect = self.image.current.get_rect(midbottom=(x, y))

    def fly(self):
        if shared_data.allow_animation:
            self.index += self.animation_speed * shared_data.dt
            if self.index >= len(self.animation):
                self.index = 0

        self.image = self.animation[int(self.index)]

    def move(self):
        self.rect.x -= shared_data.velocity + 2
    
    def redraw(self):
        self.image.get_state(shared_data.time_state)

        if self.rect.left <= const.WIDTH:
            self.fly()
            ds.screen.blit(self.image.current, self.rect)

    def change_pos(self, x: int):
        self.rect.centerx = x
        self.rect.bottom = randint(shared_data.GROUND_Y_VALUE - 100, shared_data.GROUND_Y_VALUE)