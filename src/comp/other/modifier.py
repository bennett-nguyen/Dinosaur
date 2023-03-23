import pygame as pg
from src.preload.settings import *


class Modifier:
    def __init__(self, game):
        self.game = game

        self.dino_velocity = 0
        self.vel_increment = 0
        self.dist_increment = 0

    def reset(self):
        self.dino_velocity = 0
        self.vel_increment = 0
        self.dist_increment = 0


class GlobalFlag:
    def __init__(self, game):
        self.game = game

        self.is_lose = False
        self.play_animation = False
        self.trigger_main_game = True

    def reset(self):
        self.is_lose = False
        self.play_animation = False
        self.trigger_main_game = True

    @property
    def trigger_subprocess(self):
        return self.game.paused_screen.run or self.game.lost_screen.run
