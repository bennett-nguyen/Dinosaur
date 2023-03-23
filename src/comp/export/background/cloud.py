import pygame as pg
from src.preload.settings import *
from src.preload.utilities import ImageState

class Cloud:
    def __init__(self, game, image: ImageState, rect: pg.Rect):
        self.game = game
        
        # Images
        self.image = image
        self.rect = rect

    def move(self):
        self.rect.x -= round((CLOUD_VELOCITY + self.game.modifier.vel_increment) * self.game.delta_time)
        if self.rect.right <= 0:
            self.rect.left = WIDTH

    def draw(self):
        if self.rect.left <= WIDTH:
            self.image.get_state(self.game.time_state)
            self.game.screen.blit(self.image.current, self.rect)

    def update(self):
        if not self.game.global_flag.trigger_subprocess:
            self.move()
        self.draw()