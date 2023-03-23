import pygame as pg
import src.preload.assets as assets
from src.preload.settings import *
from src.preload.utilities import ImageState


class Process:
    def __init__(self, game, message: str, button_image: ImageState):
        self.game = game

        # Flag
        self.run = False
        
        # Images & Text
        self.message = message
        self.font = assets.CustomFont.get_font('PressStart2P', 35)
        self.button = button_image
        self.button_rect = self.button.current.get_rect(center=(HALF_WIDTH, HALF_HEIGHT))

        self.title = self.font.render(self.message, True, DAY_TEXT_COLOR)
        self.title_rect = self.title.get_rect(center=(self.button_rect.centerx, self.button_rect.centery - 100))

    def button_on_click(self):
        if self.button_rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            self.run = False
            self.game.clock.tick(FPS)
            self.on_click_event()

    def change_state(self):
        color = DAY_TEXT_COLOR if self.game.time_state == DAY else NIGHT_TEXT_COLOR
        self.title = self.font.render(self.message, True, color)
        self.button.get_state(self.game.time_state)

    def activate(self):
        self.change_state()
        self.game.screen.blit(self.button.current, self.button_rect)
        self.game.screen.blit(self.title, self.title_rect)

        self.button_on_click()

    def on_click_event(self):
        pass
