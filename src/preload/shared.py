import pygame as pg
import src.preload.constant as const
from json import load
from dataclasses import dataclass


with open('./config.json', 'r') as f:
    config = load(f)
    if config['timeState'].lower() not in [const.DAY, const.NIGHT]:
        raise ValueError('timeState only accepts these values: "day", "night"')

@dataclass(eq=False, unsafe_hash=False, frozen=True)
class __Cache:
    '''
    Defines data that are loaded from config.json
    '''
    time_state: str = config['timeState'].lower()

@dataclass(eq=False, unsafe_hash=False)
class __SharedData:
    """
    Defines the data that will be shared across all components
    """
    dt: float
    events: pg.event
    time_state: str
    velocity: int
    is_lose: bool
    allow_animation: bool
    paused_delay: float
    velocity_incrementer: int
    distance_incrementer: int
    GROUND_Y_VALUE: int

cache = __Cache()
shared_data = __SharedData(None, None, cache.time_state, 0, False, True, 0, 0, 0, 0)
