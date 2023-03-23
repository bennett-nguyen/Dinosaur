import pygame as pg

from typing import List
from random import choices
from src.preload.settings import *
from src.comp.export.pool_comp.cactus import Cactus
from src.comp.export.pool_comp.pteranodon import Pteranodon
from src.comp.export.pool import _init_cactii_pool, _init_pteranodon_pool, Pool


class ObstacleManager:
    def __init__(self, game):
        self.game = game
        self.cactii_pool = Pool(_init_cactii_pool, game)
        self.pteranodon_pool = Pool(_init_pteranodon_pool, game)

        self.obstacles: List[Cactus, Pteranodon] = []
        self.generate_to_object = [CACTUS, PTERANODON]

    def move_obstacle(self):
        for obstacle in self.obstacles[:]:
            obstacle.move()

            if obstacle.rect.right < 0:
                if obstacle.id == CACTUS:
                    self.cactii_pool.release_object(obstacle)
                elif obstacle.id == PTERANODON:
                    self.pteranodon_pool.release_object(obstacle)

                self.obstacles.remove(obstacle)

    def redraw_obstacle(self):
        for obstacle in self.obstacles:
            if obstacle.rect.left >= WIDTH:
                continue
            obstacle.redraw()

    def update(self):
        self.generate_object()
        if not self.game.global_flag.trigger_subprocess:
            self.move_obstacle()
        self.redraw_obstacle()

    def generate_object(self):
        if len(self.obstacles) >= MAX_OBSTACLE:
            return

        if not len(self.obstacles):
            cactus = self.cactii_pool.get_object()
            cactus.rect.centerx = WIDTH + 100
            self.obstacles.append(cactus)

        generate_obstacle_type = choices([CACTUS, PTERANODON], weights=[8, 2])[0]

        for _ in range(MAX_OBSTACLE - len(self.obstacles)):
            static_point = self.obstacles[-1].rect.right

            if generate_obstacle_type == CACTUS:
                cactus = self.cactii_pool.get_object()
                distance_between_object = CLOSE_OBSTACLE_DISTANCE if cactus.is_standalone_object else FAR_OBSTACLE_DISTANCE
                cactus.change_pos(static_point + distance_between_object + self.game.modifier.dist_increment)
                self.obstacles.append(cactus)

            elif generate_obstacle_type == PTERANODON:
                ptenarodon = self.pteranodon_pool.get_object()
                ptenarodon.change_pos(static_point + PTERANODON_DISTANCE + self.game.modifier.dist_increment)
                self.obstacles.append(ptenarodon)

    def reset(self):
        for obstacle in self.obstacles:
            if obstacle.id == PTERANODON:
                self.pteranodon_pool.release_object(obstacle)
            else:
                self.cactii_pool.release_object(obstacle)

        self.obstacles.clear()
