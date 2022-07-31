import pygame as pg
import src.preload.ds as ds
import src.preload.assets as assets
import src.preload.constant as const
from src.preload.shared import shared_data

class Moon:
    def __init__(self):
        self.alpha = const.MOON_ALPHA
        self.moon_stages_img = assets.Gallery.MOON
        self.stages = ('waxing-crescent', 'waxing-crescent-wider', 'first-quarter', 'full-moon', 'third-quarter', 'waning-crescent-wider', 'waning-crescent', 'new-moon')
        self.index = -1
        self.current_state = None
        self.surf = None
        self.rect = self.moon_stages_img[self.stages[3]].get_rect(center=(1070, 100))
    
    def draw(self):
        self.current_state = self.stages[self.index]
        self.surf = self.moon_stages_img[self.current_state]

        self.change_alpha()
        ds.screen.blit(self.surf, self.rect)

    def change_alpha(self):
        if self.alpha > 0 and shared_data.time_state == 'day':
            self.alpha -= 5
        elif self.alpha < const.MOON_ALPHA and shared_data.time_state == 'night':
            self.alpha += 5
            self.alpha = min(self.alpha, const.MOON_ALPHA)

        self.surf.set_alpha(self.alpha)

    # def control(self):
    #     for event in shared_data.events:
    #         if event.type == pg.KEYDOWN:
    #             if event.key == pg.K_LEFT:
    #                 self.rect.x -= 10
    #             elif event.key == pg.K_RIGHT:
    #                 self.rect.x += 10
    #             elif event.key == pg.K_a:
    #                 self.index += 1
    #                 if self.index > len(self.stages) - 1:
    #                     self.index = 0
    #             elif event.key == pg.K_d:
    #                 self.index -= 1
    #                 if self.index < 0:
    #                     self.index = len(self.stages) - 1