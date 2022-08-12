import pygame as pg
import src.preload.assets as assets
from src.preload.shared import shared_data, cache
from src.comp.export.sub_process import Process


class LostScreen(Process):
    def __init__(self, _f):
        super().__init__('G A M E  O V E R', assets.Gallery.RETRY_BUTTON)
        self._reset_function = _f

    def on_click_event(self):
        shared_data.distance_incrementer = shared_data.velocity_incrementer = shared_data.paused_delay = 0
        shared_data.time_state = cache.time_state
        self._reset_function()
        shared_data.is_lose = False
