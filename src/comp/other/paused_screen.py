import pygame as pg
import src.preload.ds as ds
import src.preload.assets as assets
import src.preload.constant as const
from src.preload.shared import shared_data

class PausedScreen:
    def __init__(self):
        self.run = False
        self.font = assets.CustomFont.get_font('PressStart2P', 35)
        self.button = assets.Gallery.CONTINUE_BUTTON
        self.button_rect = self.button.current.get_rect(center=(const.HALF_WIDTH, const.HALF_HEIGHT))
        
        self.title = self.font.render('P A U S E D', True, const.DAY_MESSAGE_COLOR)
        self.title_rect = self.title.get_rect(center=(self.button_rect.centerx, self.button_rect.centery - 100))
        
        self.paused_time = 0
        self.current_time = 0
        self.paused_delay = 0

    def button_on_click(self):
        if self.button_rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            self.run = False
            ds.clock.tick(const.FPS)
            self.paused_delay = self.current_time - self.paused_time

    def change_title_color(self, color):
        self.title = self.font.render('P A U S E D', True, color)

    def activate_pause_screen(self):
        self.current_time = pg.time.get_ticks()
        self.button.get_state(shared_data.time_state)

        ds.screen.blit(self.button.current, self.button_rect)
        ds.screen.blit(self.title, self.title_rect)

        self.button_on_click()
