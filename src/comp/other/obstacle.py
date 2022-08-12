import pygame as pg
import src.preload.constant as const
from random import choices
from src.preload.shared import shared_data
from src.comp.export.pool_comp.cactus import Cactus
from src.comp.export.pool_comp.pteranodon import Pteranodon
from src.comp.export.pool import cacti_pool, pteranodon_pool
from typing import List


class ObstacleGenerator:
    def __init__(self):
        self.obstacles: List[Cactus, Pteranodon] = []
        self.generate_to_object = [const.CACTUS, const.PTERANODON]
        self.pteranodon_pool = pteranodon_pool
        self.cacti_pool = cacti_pool

    def move_obstacle(self):
        for obstacle in self.obstacles[:]:
            obstacle.move()

            if obstacle.rect.right < 0:
                if obstacle.id == const.CACTUS:
                    self.cacti_pool.release_object(obstacle)
                elif obstacle.id == const.PTERANODON:
                    self.pteranodon_pool.release_object(obstacle)

                self.obstacles.remove(obstacle)

    def redraw_obstacle(self):
        for obstacle in self.obstacles[:]:
            if obstacle.rect.left < const.WIDTH:
                obstacle.redraw()

    def generate_object(self):
        if len(self.obstacles) >= const.MAX_OBSTACLE:
            return

        if not len(self.obstacles):
            cactus = self.cacti_pool.get_object()
            cactus.rect.centerx = const.WIDTH + 100
            self.obstacles.append(cactus)

        generate_obstacle_type = choices([const.CACTUS, const.PTERANODON], weights=[8, 2])[0]

        for _ in range(const.MAX_OBSTACLE - len(self.obstacles)):
            static_point = self.obstacles[-1].rect.right

            if generate_obstacle_type == const.CACTUS:
                cactus = self.cacti_pool.get_object()
                distance_between_object = const.CLOSE_OBSTACLE_DISTANCE if cactus.is_standalone_object else const.FAR_OBSTACLE_DISTANCE
                cactus.change_pos(static_point + distance_between_object + shared_data.distance_incrementer)
                self.obstacles.append(cactus)

            elif generate_obstacle_type == const.PTERANODON:
                ptenarodon = pteranodon_pool.get_object()
                ptenarodon.change_pos(static_point + const.PTERANODON_DISTANCE + shared_data.distance_incrementer)
                self.obstacles.append(ptenarodon)

    def reset(self):
        for obstacle in self.obstacles:
            if obstacle.id == const.PTERANODON:
                self.pteranodon_pool.release_object(obstacle)
            else:
                self.cacti_pool.release_object(obstacle)

        self.obstacles.clear()
