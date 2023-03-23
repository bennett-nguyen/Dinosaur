import pygame as pg
import src.preload.assets as assets
from src.preload.settings import *
from src.preload.utilities import Timer

from random import choice
from src.comp.export.background.star import Star
from src.comp.export.background.moon import Moon
from src.comp.export.background.cloud import Cloud


class Background:
    def __init__(self, game):
        self.game = game
        self.observers = []

        # Timers
        self.cycle_delay = DAY_NIGHT_CYCLE_DELAY * 1000
        self.cycle_timer = Timer(self.cycle_delay)

        # Flags
        self.is_transforming_state = False
        self.done_transforming_text_color = False
        self.done_transforming_screen_color = False

        if self.game.time_state == DAY:
            self.transform_to = NIGHT
            self.background_color = DAY_BG_COLOR
            self.text_color = DAY_TEXT_COLOR
        else:
            self.transform_to = DAY
            self.background_color = NIGHT_BG_COLOR
            self.text_color = NIGHT_TEXT_COLOR

        self.new_background()

    def new_background(self):
        # Ground
        self.ground = self.ground_2 = assets.Gallery.GROUND
        self.ground.get_state(self.game.time_state)
        self.ground_2.get_state(self.game.time_state)
        self.ground_rect = self.ground.current.get_rect(bottomleft=(0, HEIGHT - GROUND_POS_Y_OFFSET))
        self.ground_2_rect = self.ground_2.current.get_rect(bottomleft=(self.ground_rect.right, self.ground_rect.bottom))

        self.object_y = self.ground_rect.top + DINO_POS_Y_OFFSET

        # Moon
        self.moon = Moon(self.game)

        # Clouds & Stars
        self.clouds: list[Cloud] = [0] * CLOUDS_AMOUNT
        self.stars: list[Star] = [0] * STARS_AMOUNT

        star_coords = ((68, 119), (349, 144), (107, 75), (478, 97), (274, 148), (908, 91), (1169, 87), (835, 68), (741, 81), (1179, 108))
        self.cloud_coords = ((2170, 108), (1657, 57), (1877, 137), (1304, 70), (1549, 65), (2013, 93))

        for i in range(CLOUDS_AMOUNT):
            surf = assets.Gallery.CLOUD
            rect = surf.current.get_rect(center=self.cloud_coords[i])
            cloud = Cloud(self.game, surf, rect)
            self.clouds[i] = cloud

        for i in range(STARS_AMOUNT):
            surf = choice(assets.Gallery.STARS)
            if self.game.time_state == DAY:
                surf.set_alpha(0)
            elif self.game.time_state == NIGHT:
                surf.set_alpha(STAR_ALPHA)

            rect = surf.get_rect(center=star_coords[i])
            star = Star(self.game, surf, rect)
            self.stars[i] = star

    def _draw_moon_n_stars(self):
        self.moon.draw()
        for star in self.stars:
            star.draw()

    def _draw_ground(self):
        self.game.screen.blit(self.ground.current, self.ground_rect)
        self.game.screen.blit(self.ground_2.current, self.ground_2_rect)

    def _draw_clouds(self):
        for cloud in self.clouds:
            cloud.update()

    def _move_ground(self):
        self.game.modifier.dino_velocity = round((DINO_VELOCITY + self.game.modifier.vel_increment) * self.game.delta_time)
        self.ground_rect.left -= self.game.modifier.dino_velocity
        self.ground_2_rect.left -= self.game.modifier.dino_velocity

        if self.ground_rect.right <= 0:
            self.ground_rect.left = self.ground_2_rect.right
        elif self.ground_2_rect.right <= 0:
            self.ground_2_rect.left = self.ground_rect.right

    def update(self):
        self.game.screen.fill(self.background_color)

        if self.game.global_flag.trigger_main_game:
            if not self.game.global_flag.trigger_subprocess:
                self._day_night_cycle()
                self._move_ground()
            self._draw_moon_n_stars()
            self._draw_clouds()

        self._draw_ground()

    def _day_night_cycle(self):
        self.cycle_timer.set_current_time()

        if not self.cycle_timer.static_point:
            self.cycle_timer.set_static_point()

        if self.cycle_timer.timer() and not self.is_transforming_state:
            self.transform_to = NIGHT if self.game.time_state == DAY else DAY
            self.is_transforming_state = True
            self.cycle_timer.set_static_point()
            self.cycle_timer.reset_paused_delay()

        if self.is_transforming_state:
            if self.transform_to == DAY:
                self._transform_day()

            elif self.transform_to == NIGHT:
                self._transform_night()

        if self.done_transforming_screen_color and self.done_transforming_text_color:
            self.is_transforming_state = self.done_transforming_screen_color = self.done_transforming_text_color = False

    def _transform_day(self):
        speed = round(COLOR_TRANSITION_SPEED * self.game.delta_time)
        change = pg.Color(int(speed), int(speed), int(speed))

        if not self.done_transforming_screen_color:
            self.background_color += change

            if self.background_color.r >= DAY_BG_COLOR.r // 1.5:
                self._change_state()
            if self.background_color.r >= DAY_BG_COLOR.r:
                self.done_transforming_screen_color = True
                self.background_color = DAY_BG_COLOR

        if not self.done_transforming_text_color:
            self.text_color -= change

            if self.text_color.r <= DAY_TEXT_COLOR.r:
                self.done_transforming_text_color = True
                self.text_color = DAY_TEXT_COLOR

    def _transform_night(self):
        speed = round(COLOR_TRANSITION_SPEED * self.game.delta_time)
        change = pg.Color(int(speed), int(speed), int(speed))

        if not self.done_transforming_screen_color:
            self.background_color -= change

            if self.background_color.r <= DAY_BG_COLOR.r // 1.5:
                self._change_state()
            if self.background_color.r <= NIGHT_BG_COLOR.r:
                self.done_transforming_screen_color = True
                self.background_color = NIGHT_BG_COLOR

        if not self.done_transforming_text_color:
            self.text_color += change

            if self.text_color.r >= NIGHT_TEXT_COLOR.r:
                self.done_transforming_text_color = True
                self.text_color = NIGHT_TEXT_COLOR

    def _change_state(self):
        self.game.time_state = self.transform_to
        self.ground.get_state(self.game.time_state)
        self.ground_2.get_state(self.game.time_state)
        self.game.score_system.change_state()

    def reset(self):
        if self.game.config["timeState"] == DAY:
            self.transform_to = NIGHT
            self.message_color = DAY_TEXT_COLOR
            self.background_color = DAY_BG_COLOR
            alpha = 0
            index = -1

        else:
            self.transform_to = DAY
            self.message_color = NIGHT_TEXT_COLOR
            self.background_color = NIGHT_BG_COLOR
            alpha = 255
            index = 0

        self.moon.index = index
        self.moon.alpha = alpha
        self.moon.surf.set_alpha(alpha)

        for star in self.stars:
            star.alpha = alpha
            star.image.set_alpha(alpha)

        for cloud, coords in zip(self.clouds, self.cloud_coords):
            cloud.rect.center = coords

        self.ground.get_state(self.game.config["timeState"])
        self.ground_2.get_state(self.game.config["timeState"])
        self.is_transforming_state = False

        self.cycle_timer.reset_timer()
