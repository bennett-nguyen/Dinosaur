import pygame as pg
from src.preload.settings import DAY, NIGHT
from typing import Optional, Union, List, Callable, Any, Optional


class ImageState:
    def __init__(self, day_image: pg.Surface, night_image: pg.Surface, init_mask: bool = False):
        self.day_image = day_image
        self.night_image = night_image

        self.current = self.day_image

        if init_mask:
            self.mask = pg.mask.from_surface(self.current)

    def get_state(self, code):
        if code == DAY:
            self.current = self.day_image
        elif code == NIGHT:
            self.current = self.night_image
        else:
            raise ValueError("Invalid code!")


class Timer:
    '''
    Standard timer for pygame
    '''

    def __init__(self, length_of_timer):
        self.current_time = 0
        self.static_point = 0
        self.length_of_timer = length_of_timer
        self.paused_delay = 0

    def set_static_point(self):
        self.static_point = pg.time.get_ticks()

    def set_current_time(self):
        self.current_time = pg.time.get_ticks()

    def reset_paused_delay(self):
        self.paused_delay = 0

    def timer(self, length_buffer: Optional[Union[int, float]] = 0) -> bool:
        return self.current_time - self.static_point > self.length_of_timer + length_buffer + self.paused_delay

    def reset_timer(self):
        self.paused_delay = 0
        self.current_time = self.static_point = pg.time.get_ticks()


class MultiTimer:
    def __init__(self, length_of_timers: List[Union[int, float]]):
        self.length_of_timers = length_of_timers
        self.index = 0
        self.current_timer = self.length_of_timers[self.index]
        self.current_time = 0
        self.static_point = 0

    def set_static_point(self):
        self.static_point = pg.time.get_ticks()

    def set_current_time(self):
        self.current_time = pg.time.get_ticks()

    def timer(self) -> bool:
        return self.current_time - self.static_point > self.current_timer

    def switch_timer(self):
        self.index += 1
        if self.index > len(self.length_of_timers) - 1:
            self.index = 0
        self.current_timer = self.length_of_timers[self.index]
