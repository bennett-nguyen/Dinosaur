import pygame as pg
from json import load
from dataclasses import dataclass


with open('./config.json', 'r') as f:
    config = load(f)

@dataclass(eq=False, unsafe_hash=False)
class __SharedData:
    """
    Defines the data that will be shared across all components
    """
    dt: float
    events: pg.event
    time_state: str


shared_data = __SharedData(None, None, config['timeState'])
