import pygame as pg
import src.preload.assets as assets
from src.preload.shared import shared_data
from src.comp.export.sub_process import Process

class PausedScreen(Process):
    def __init__(self):
        super().__init__('P A U S E D', assets.Gallery.CONTINUE_BUTTON)
        self.paused_time = 0
        self.current_time = 0
        self.paused_delay = 0

    def on_click_event(self):
        self.paused_delay = self.current_time - self.paused_time
        shared_data.allow_animation = True
    
    def activate(self):
        self.current_time = pg.time.get_ticks()
        super().activate()
