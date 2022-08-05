import pygame as pg
import src.preload.constant as const
from random import choices, choice
from src.preload.shared import shared_data
from src.comp.export.cactus import cacti, Cactus
from src.comp.export.pteranodon import Pteranodon

class ObstacleGenerator:
    def __init__(self):
        self.obstacles: list[Cactus, Pteranodon] = []
        self.generate_to_object = [const.CACTUS, const.PTERANODON]

    def move_and_redraw_obstacle(self):
        for obstacle in self.obstacles[:]:
            obstacle.move()
            if obstacle.rect.left < const.WIDTH:
                obstacle.redraw()
            
            if obstacle.rect.right < 0:
                self.obstacles.remove(obstacle)
    
    def generate_object(self):
        if len(self.obstacles) >= const.MAX_OBSTACLE:
            return

        if len(self.obstacles) == 0:
            cactus_image = choice(cacti)
            cactus = Cactus(cactus_image)
            cactus.init_pos(const.WIDTH + 50)
            self.obstacles.append(cactus)

        generate_obstacle_type = choices([const.CACTUS, const.PTERANODON], weights=[8, 2])[0]
        for _ in range(const.MAX_OBSTACLE - len(self.obstacles)):
            static_point = self.obstacles[-1].rect.right

            if generate_obstacle_type == const.CACTUS:
                cactus_image = choice(cacti)
                cactus = Cactus(cactus_image)
                distance_between_object = const.CLOSE_OBSTACLE_DISTANCE if cactus.is_standalone_object else const.FAR_OBSTACLE_DISTANCE
                cactus.init_pos(static_point + distance_between_object + shared_data.distance_incrementer)
                self.obstacles.append(cactus)

            elif generate_obstacle_type == const.PTERANODON:
                ptenarodon = Pteranodon()
                ptenarodon.init_pos(static_point + const.PTERANODON_DISTANCE + shared_data.distance_incrementer)
                self.obstacles.append(ptenarodon)