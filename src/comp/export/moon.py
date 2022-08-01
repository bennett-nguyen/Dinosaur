import pygame as pg
import src.preload.ds as ds
import src.preload.assets as assets
import src.preload.constant as const
from src.preload.shared import shared_data

class Moon:
    def __init__(self):
        self.alpha = const.MOON_ALPHA if shared_data.time_state == const.NIGHT else 0
        self.moon_stages_img = assets.Gallery.MOON
        self.stages = ('waxing-crescent', 'waxing-crescent-wider', 'first-quarter', 'full-moon', 'third-quarter', 'waning-crescent-wider', 'waning-crescent', 'new-moon')
        self.index = -1
        self.current_state = None
        self.surf = None
        self.rect = self.moon_stages_img[self.stages[3]].get_rect(center=(1070, 100))
        self.alpha_modifier = 270

    def draw(self):
        self.current_state = self.stages[self.index]
        self.surf = self.moon_stages_img[self.current_state]

        self.change_alpha()
        ds.screen.blit(self.surf, self.rect)

    def change_alpha(self):
        modifier = round(self.alpha_modifier * shared_data.dt)

        if self.alpha > 0 and shared_data.time_state == const.DAY:
            self.alpha -= modifier
        elif self.alpha < const.MOON_ALPHA and shared_data.time_state == const.NIGHT:
            self.alpha += modifier
            self.alpha = min(self.alpha, const.MOON_ALPHA)

        self.surf.set_alpha(self.alpha)
