import time
import pygame as pg
import src.preload.assets as assets
from src.comp.export.sub_process import Process
from typing import Callable, Any


class PausedScreen(Process):
    def __init__(self, game):
        super().__init__(game, 'P A U S E D', assets.Gallery.CONTINUE_BUTTON)
        self.paused_time = 0
        self.current_time = 0

    def on_click_event(self):
        paused_delay = self.current_time - self.paused_time
        self.game.background.cycle_timer.paused_delay += paused_delay

        if self.game.score_system.reached_milestone:
            self.game.score_system.animation_timer.paused_delay += paused_delay

    def activate(self):
        self.current_time = pg.time.get_ticks()
        super().activate()
