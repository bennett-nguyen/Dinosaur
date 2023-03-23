import pygame as pg
import src.preload.assets as assets
from random import randint
from src.preload.settings import *


class Pteranodon:
    def __init__(self, game):
        self.game = game

        # Images
        self.animation = [assets.Gallery.PTERANODON_FLYING_1, assets.Gallery.PTERANODON_FLYING_2]
        self.image = self.animation[0]
        x = WIDTH + 200
        y = randint(self.game.background.object_y - 100, self.game.background.object_y)
        self.rect = self.image.current.get_rect(midbottom=(x, y))

        # Flag
        self.is_standalone_object = True

        # Animation
        self.index = 0
        self.animation_speed = 6

        self.id = PTERANODON

    def fly(self):
        if not self.game.global_flag.trigger_subprocess:
            self.index += self.animation_speed * self.game.delta_time
            if self.index >= len(self.animation):
                self.index = 0

        self.image = self.animation[int(self.index)]

    def move(self):
        self.rect.x -= self.game.modifier.dino_velocity + 2

    def redraw(self):
        self.image.get_state(self.game.time_state)

        if self.rect.left <= WIDTH:
            self.fly()
            self.game.screen.blit(self.image.current, self.rect)

    def change_pos(self, x: int):
        self.rect.centerx = x
        self.rect.bottom = randint(self.game.background.object_y - 100, self.game.background.object_y)
