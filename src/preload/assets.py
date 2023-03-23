import pygame as pg
from dataclasses import dataclass
from src.preload.utilities import ImageState
from src.preload.spritesheet import Spritesheet


@dataclass(frozen=True, init=True, eq=False, unsafe_hash=False)
class _Font:
    FONT_MAP = {
        "PressStart2P": "./assets/font/PressStart2P-Regular.ttf"
    }

    def get_font(self, name: str, size: int):
        """
        Available fonts: 
        - PressStart2P

        Standard size:
        - title font 1: 100
        - title font 2: 75
        - title font 3: 50
        - menu score: 20
        """
        return pg.font.Font(self.FONT_MAP[name], size)


CustomFont = _Font()

_ground_ss = Spritesheet('./assets/img/spritesheets/ground/ground.png')
_cactus_ss = Spritesheet('./assets/img/spritesheets/cactus/cactus.png')
_dinosaur_ss = Spritesheet('./assets/img/spritesheets/dino/dinosaur.png')
_pteranodon_ss = Spritesheet('./assets/img/spritesheets/pteranodon/pteranodon.png')

_cloud_ss = Spritesheet('./assets/img/spritesheets/cloud/cloud.png')
_star_ss = Spritesheet('./assets/img/spritesheets/star/stars.png')
_moon_ss = Spritesheet('./assets/img/spritesheets/moon/moon.png')
_continue_button_ss = Spritesheet('./assets/img/spritesheets/continue/continue.png')
_retry_button_ss = Spritesheet('./assets/img/spritesheets/retry/retry.png')


@dataclass(frozen=True, eq=False, unsafe_hash=False, init=False)
class Gallery:
    GROUND = ImageState(_ground_ss.parse_sprite('day_ground.png'), _ground_ss.parse_sprite('night_ground.png'))

    DINO_BLINK = ImageState(_dinosaur_ss.parse_sprite('day_blink.png'), _dinosaur_ss.parse_sprite('night_blink.png'))
    DINO_IDLE = ImageState(_dinosaur_ss.parse_sprite('day_idle.png'), _dinosaur_ss.parse_sprite('night_idle.png'), True)
    DINO_RUNNING_1 = ImageState(_dinosaur_ss.parse_sprite('day_running1.png'), _dinosaur_ss.parse_sprite('night_running1.png'), True)
    DINO_RUNNING_2 = ImageState(_dinosaur_ss.parse_sprite('day_running2.png'), _dinosaur_ss.parse_sprite('night_running2.png'), True)
    DINO_DUCK_1 = ImageState(_dinosaur_ss.parse_sprite('day_dino_duck_1.png'), _dinosaur_ss.parse_sprite('night_dino_duck_1.png'), True)
    DINO_DUCK_2 = ImageState(_dinosaur_ss.parse_sprite('day_dino_duck_2.png'), _dinosaur_ss.parse_sprite('night_dino_duck_2.png'), True)
    DINO_DEAD = ImageState(_dinosaur_ss.parse_sprite('day_dead.png'), _dinosaur_ss.parse_sprite('night_dead.png'))

    CLOUD = ImageState(_cloud_ss.parse_sprite('day_cloud.png'), _cloud_ss.parse_sprite('night_cloud.png'))
    STARS = (_star_ss.parse_sprite('star_1.png'), _star_ss.parse_sprite('star_2.png'), _star_ss.parse_sprite('star_3.png'))
    MOON = {
        'waxing-crescent': _moon_ss.parse_sprite('waxing-crescent.png'),
        'waxing-crescent-wider': _moon_ss.parse_sprite('waxing-crescent-wider.png'),
        'first-quarter': _moon_ss.parse_sprite('first-quarter.png'),
        'full-moon': _moon_ss.parse_sprite('full-moon.png'),
        'third-quarter': _moon_ss.parse_sprite('third-quarter.png'),
        'waning-crescent-wider': _moon_ss.parse_sprite('waning-crescent-wider.png'),
        'waning-crescent': _moon_ss.parse_sprite('waning-crescent.png'),
        'new-moon': pg.Surface((1, 1), pg.SRCALPHA, 32)
    }

    SMALL_CACTUS_1 = ImageState(_cactus_ss.parse_sprite('day_small_cactus_1.png'), _cactus_ss.parse_sprite('night_small_cactus_1.png'))
    SMALL_CACTUS_2 = ImageState(_cactus_ss.parse_sprite('day_small_cactus_2.png'), _cactus_ss.parse_sprite('night_small_cactus_2.png'))
    SMALL_CACTUS_3 = ImageState(_cactus_ss.parse_sprite('day_small_cactus_3.png'), _cactus_ss.parse_sprite('night_small_cactus_3.png'))
    SMALL_CACTUS_4 = ImageState(_cactus_ss.parse_sprite('day_small_cactus_4.png'), _cactus_ss.parse_sprite('night_small_cactus_4.png'))

    BIG_CACTUS_1 = ImageState(_cactus_ss.parse_sprite('day_big_cactus_1.png'), _cactus_ss.parse_sprite('night_big_cactus_1.png'))
    BIG_CACTUS_2 = ImageState(_cactus_ss.parse_sprite('day_big_cactus_2.png'), _cactus_ss.parse_sprite('night_big_cactus_2.png'))
    BIG_CACTUS_3 = ImageState(_cactus_ss.parse_sprite('day_big_cactus_3.png'), _cactus_ss.parse_sprite('night_big_cactus_3.png'))
    BIG_CACTUS_4 = ImageState(_cactus_ss.parse_sprite('day_big_cactus_5.png'), _cactus_ss.parse_sprite('night_big_cactus_5.png'))
    BIG_CACTUS_WITH_SMALL_CACTUS = ImageState(_cactus_ss.parse_sprite('day_big_cactus_4.png'), _cactus_ss.parse_sprite('night_big_cactus_4.png'))

    PTERANODON_FLYING_1 = ImageState(_pteranodon_ss.parse_sprite('day_pteranodon_flying_1.png'), _pteranodon_ss.parse_sprite('night_pteranodon_flying_1.png'), True)
    PTERANODON_FLYING_2 = ImageState(_pteranodon_ss.parse_sprite('day_pteranodon_flying_2.png'), _pteranodon_ss.parse_sprite('night_pteranodon_flying_2.png'), True)

    CONTINUE_BUTTON = ImageState(_continue_button_ss.parse_sprite('day_continue_button.png'), _continue_button_ss.parse_sprite('night_continue_button.png'))
    RETRY_BUTTON = ImageState(_retry_button_ss.parse_sprite('day_retry_button.png'), _retry_button_ss.parse_sprite('night_retry_button.png'))


@dataclass(frozen=True, eq=False, unsafe_hash=False, init=False)
class Audio:
    JUMP = pg.mixer.Sound('./assets/sfx/jump.ogg')
    DEATH = pg.mixer.Sound('./assets/sfx/death.ogg')
    REACHED_MILESTONE = pg.mixer.Sound('./assets/sfx/score.ogg')
