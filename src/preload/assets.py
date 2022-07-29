import pygame as pg
from src.preload.comp import ImageState
from dataclasses import dataclass
from src.preload.spritesheet import Spritesheet


@dataclass(frozen=True, init=True, eq=False, unsafe_hash=False)
class __Font:
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

CustomFont = __Font()

ground_ss = Spritesheet('./assets/img/spritesheets/ground/ground.png')
dinosaur_ss = Spritesheet('./assets/img/spritesheets/dino/dinosaur.png')

cloud_ss = Spritesheet('./assets/img/spritesheets/cloud/cloud.png')
star_ss = Spritesheet('./assets/img/spritesheets/star/stars.png')
moon_ss = Spritesheet('./assets/img/spritesheets/moon/moon.png')

@dataclass(frozen=True, eq=False, unsafe_hash=False, init=False)
class Gallery:
    GROUND = ImageState(ground_ss.parse_sprite('day_ground.png'), ground_ss.parse_sprite('night_ground.png'))

    DINO_BLINK = ImageState(dinosaur_ss.parse_sprite('day_blink.png'), dinosaur_ss.parse_sprite('night_blink.png'))
    DINO_IDLE = ImageState(dinosaur_ss.parse_sprite('day_idle.png'), dinosaur_ss.parse_sprite('night_idle.png'))
    DINO_RUNNING_1 = ImageState(dinosaur_ss.parse_sprite('day_running1.png'), dinosaur_ss.parse_sprite('night_running1.png'))
    DINO_RUNNING_2 = ImageState(dinosaur_ss.parse_sprite('day_running2.png'), dinosaur_ss.parse_sprite('night_running2.png'))
    DINO_DODGE_1 = ImageState(dinosaur_ss.parse_sprite('day_dino_dodge_1.png'), dinosaur_ss.parse_sprite('night_dino_dodge_1.png'))
    DINO_DODGE_2 = ImageState(dinosaur_ss.parse_sprite('day_dino_dodge_2.png'), dinosaur_ss.parse_sprite('night_dino_dodge_2.png'))
    DINO_DEAD = ImageState(dinosaur_ss.parse_sprite('day_dead.png'), dinosaur_ss.parse_sprite('night_dead.png'))

    CLOUD = ImageState(cloud_ss.parse_sprite('day_cloud.png'), cloud_ss.parse_sprite('night_cloud.png'))
    STARS = (star_ss.parse_sprite('star_1.png'), star_ss.parse_sprite('star_2.png'), star_ss.parse_sprite('star_3.png'))
    MOON = {
        'waxing-crescent': moon_ss.parse_sprite('waxing-crescent.png'),
        'waxing-crescent-wider': moon_ss.parse_sprite('waxing-crescent-wider.png'),
        'first-quarter': moon_ss.parse_sprite('first-quarter.png'),
        'full-moon': moon_ss.parse_sprite('full-moon.png'),
        'third-quarter': moon_ss.parse_sprite('third-quarter.png'),
        'waning-crescent-wider': moon_ss.parse_sprite('waning-crescent-wider.png'),
        'waning-crescent': moon_ss.parse_sprite('waning-crescent.png'),
        'new-moon': pg.Surface((1, 1), pg.SRCALPHA, 32)
    }

@dataclass(frozen=True, eq=False, unsafe_hash=False, init=False)
class Audio:
    JUMP = pg.mixer.Sound('./assets/sfx/jump.ogg')
    DEATH = pg.mixer.Sound('./assets/sfx/death.ogg')
    REACHED_MILESTONE = pg.mixer.Sound('./assets/sfx/score.ogg')