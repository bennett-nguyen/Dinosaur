import pygame as pg
import src.preload.constant as const

class ImageState:
    def __init__(self, day_image: pg.Surface, night_image: pg.Surface):
        self.day_image = day_image
        self.night_image = night_image

        self.current = self.day_image

    def get_state(self, code):
        match code:
            case const.DAY:
                self.current = self.day_image
            case const.NIGHT:
                self.current = self.night_image

BOOL_OPERATOR_LEQUAL = 0 # <=
BOOL_OPERATOR_GEQUAL = 1 # >=

def timer(current_time: float, static_point: float, length_of_timer: float, bool_operator: int) -> bool:
    if bool_operator == BOOL_OPERATOR_GEQUAL:
        return current_time - static_point >= length_of_timer
    elif bool_operator == BOOL_OPERATOR_LEQUAL:
        return current_time - static_point <= length_of_timer