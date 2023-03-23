import pygame as pg
import src.preload.assets as assets
from src.preload.settings import *


class Moon:
    def __init__(self, game):
        self.game = game

        # Images
        self.moon_stages_img = assets.Gallery.MOON
        self.stages = ('waxing-crescent', 'waxing-crescent-wider', 'first-quarter', 'full-moon', 'third-quarter', 'waning-crescent-wider', 'waning-crescent', 'new-moon')

        # Animation
        self.index = -1
        self.current_state = None

        # Image
        self.surf = None
        self.rect = self.moon_stages_img[self.stages[3]].get_rect(center=(1070, 100))

        # Transparency
        self.alpha = MOON_ALPHA if self.game.time_state == NIGHT else 0
        self.alpha_modifier = 270
        
        # Flag
        self.switched_moon_phase = False

    def update_moon_state(self):
        if self.game.time_state == NIGHT and not self.switched_moon_phase:
            self.index += 1
            self.switched_moon_phase = True
            if self.index > len(self.stages) - 1:
                self.index = 0
        elif self.game.time_state == DAY:
            self.switched_moon_phase = False

    def draw(self):
        self.update_moon_state()
        self.current_state = self.stages[self.index]
        self.surf = self.moon_stages_img[self.current_state]

        self.change_alpha()
        self.game.screen.blit(self.surf, self.rect)

    def change_alpha(self):
        modifier = round(self.alpha_modifier * self.game.delta_time)

        if self.alpha > 0 and self.game.time_state == DAY:
            self.alpha -= modifier
        elif self.alpha < MOON_ALPHA and self.game.time_state == NIGHT:
            self.alpha += modifier
            self.alpha = min(self.alpha, MOON_ALPHA)

        self.surf.set_alpha(self.alpha)
