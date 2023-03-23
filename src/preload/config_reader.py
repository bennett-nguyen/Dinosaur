import json
from src.preload.settings import *

with open('./config.json', 'r') as f:
    config = json.load(f)
    if config["timeState"].lower() not in [DAY, NIGHT]:
        raise ValueError('timeState only accepts these values: "day", "night"')

config['timeState'] = config["timeState"].lower()
