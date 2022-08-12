import pygame as pg
import src.preload.ds as ds
import src.preload.assets as assets
import src.preload.constant as const
from src.preload.comp import ImageState
from src.preload.shared import shared_data

from typing import Tuple


class Process:
    def __init__(self, message, button_image: ImageState):
        self.run = False
        self.message = message
        self.font = assets.CustomFont.get_font('PressStart2P', 35)
        self.button = button_image
        self.button_rect = self.button.current.get_rect(center=(const.HALF_WIDTH, const.HALF_HEIGHT))

        self.title = self.font.render(self.message, True, const.DAY_MESSAGE_COLOR)
        self.title_rect = self.title.get_rect(center=(self.button_rect.centerx, self.button_rect.centery - 100))

    def button_on_click(self):
        if self.button_rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            self.run = False
            ds.clock.tick(const.FPS)
            self.on_click_event()

    def change_state(self, color: Tuple[int, int, int]):
        self.title = self.font.render(self.message, True, color)
        self.button.get_state(shared_data.time_state)

    def activate(self):
        ds.screen.blit(self.button.current, self.button_rect)
        ds.screen.blit(self.title, self.title_rect)

        self.button_on_click()

    def on_click_event(self):
        pass
