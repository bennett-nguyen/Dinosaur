"""
Defines constants that are used throughout the game
"""
# doing private imports btw
from collections import namedtuple as __namedtuple

__RGB = __namedtuple('RGB', ('R', 'G', 'B'))

WIDTH: int = 1200
HEIGHT: int = 500
FPS: int = 60
PAUSED_FPS: int = 30

HALF_WIDTH: int = WIDTH/2
HALF_HEIGHT: int = HEIGHT/2

DINO_POS_X_OFFSET: int = 40
DINO_POS_Y_OFFSET: int = 20
GROUND_POS_Y_OFFSET: int = 30


DAY_SCREEN_COLOR = __RGB(255, 255, 255)
NIGHT_SCREEN_COLOR = __RGB(0, 0, 0)

DAY_MESSAGE_COLOR = __RGB(82, 82, 83)
NIGHT_MESSAGE_COLOR = __RGB(255, 255, 255)

STAR_ALPHA: int = 255
MOON_ALPHA: int = 255

CLOUDS_AMOUNT: int = 6
STARS_AMOUNT: int = 10

DAY_NIGHT_CYCLE_DELAY: float | int = 38 # in seconds

DINO_VELOCITY = 750
CLOUD_VELOCITY = 50

CLOSE_OBSTACLE_DISTANCE = 400
FAR_OBSTACLE_DISTANCE = 700
PTERANODON_DISTANCE = 1000

MAX_OBSTACLE = 3


DAY = 'day'
NIGHT = 'night'

IDLE = 'idle'
DUCK = 'duck'
RUN = 'run'
JUMP = 'jump'

PTERANODON = 'ptenarodon'
CACTUS = 'cactus'